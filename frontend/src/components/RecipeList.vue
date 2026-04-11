<template>
  <div class="recipe-list">
    <!-- 搜索栏 -->
    <div class="search-bar">
      <input
        v-model="keyword"
        type="text"
        placeholder="搜索菜谱..."
        @keyup.enter="fetchRecipes"
      />
      <button @click="fetchRecipes">搜索</button>
      <button @click="showForm = true" class="btn-add">+ 新增菜谱</button>
    </div>

    <!-- 菜谱卡片列表 -->
    <div class="recipe-grid" v-if="recipes.length">
      <div class="recipe-card" v-for="r in recipes" :key="r.id" @click="viewDetail(r.id)">
        <div class="card-header">
          <span class="tag">{{ r.category }}</span>
          <span class="difficulty" :class="r.difficulty">{{ r.difficulty }}</span>
        </div>
        <h3>{{ r.title }}</h3>
        <div class="card-info">
          <span>⏱ {{ r.cook_time }}分钟</span>
        </div>
        <div class="card-actions" @click.stop>
          <button @click="editRecipe(r)">编辑</button>
          <button @click="confirmDelete(r.id)" class="btn-delete">删除</button>
        </div>
      </div>
    </div>
    <div v-else class="empty">
      <p>暂无菜谱，试试搜索其他关键词，或点击「新增菜谱」添加。</p>
    </div>

    <!-- 分页 -->
    <div class="pagination" v-if="total > pageSize">
      <button :disabled="page === 0" @click="page--; fetchRecipes()">上一页</button>
      <span>第 {{ page + 1 }} / {{ Math.ceil(total / pageSize) }} 页</span>
      <button :disabled="(page + 1) * pageSize >= total" @click="page++; fetchRecipes()">下一页</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { recipeAPI } from '../api/recipes.js'

const emit = defineEmits(['view', 'edit', 'add'])

const recipes = ref([])
const total = ref(0)
const page = ref(0)
const pageSize = 12
const keyword = ref('')
const showForm = ref(false)

function parseJsonField(field) {
  try { return JSON.parse(field) } catch { return [] }
}

async function fetchRecipes() {
  const res = await recipeAPI.list({ skip: page.value * pageSize, limit: pageSize, keyword: keyword.value || undefined })
  recipes.value = res.data.items
  total.value = res.data.total
}

function viewDetail(id) { emit('view', id) }
function editRecipe(r) { emit('edit', r) }

async function confirmDelete(id) {
  if (!confirm('确定要删除这个菜谱吗？')) return
  await recipeAPI.delete(id)
  fetchRecipes()
}

onMounted(fetchRecipes)
</script>
