<template>
  <div id="app">
    <!-- Toast -->
    <div class="toast-container">
      <div
        v-for="t in toasts"
        :key="t.id"
        :class="['toast', `toast-${t.type}`]"
      >
        <svg v-if="t.type==='success'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        <svg v-else-if="t.type==='error'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <svg v-else viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
        {{ t.message }}
      </div>
    </div>

    <!-- 侧边栏 -->
    <aside class="sidebar">
      <div class="sidebar-brand">
        <div class="logo">
          <div class="logo-icon">🍳</div>
          <div>
            <div class="logo-text">Recipe Hub</div>
            <div class="logo-sub">菜谱管理系统</div>
          </div>
        </div>
      </div>

      <div class="sidebar-section">
        <div class="sidebar-section-label">浏览</div>
        <button
          v-for="item in navItems"
          :key="item.key"
          :class="['sidebar-item', { active: activeFilter === item.key }]"
          @click="setFilter(item.key)"
        >
          <svg v-html="item.icon"></svg>
          {{ item.label }}
          <span class="count">{{ item.count }}</span>
        </button>
      </div>

      <div class="sidebar-divider"></div>

      <div class="sidebar-section">
        <div class="sidebar-section-label">分类</div>
        <button
          v-for="cat in categories"
          :key="cat.name"
          :class="['sidebar-item', { active: activeFilter === 'category:' + cat.name }]"
          @click="setFilter('category:' + cat.name)"
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
          {{ cat.name }}
          <span class="count">{{ cat.count }}</span>
        </button>
      </div>

      <div class="sidebar-stats">
        <div class="sidebar-stat"><span>全部菜谱</span><strong>{{ totalCount }}</strong></div>
        <div class="sidebar-stat"><span>我的收藏</span><strong>{{ favoritesCount }}</strong></div>
      </div>
    </aside>

    <!-- 主内容 -->
    <div class="main-content">
      <!-- 顶部栏 -->
      <header class="topbar">
        <div class="topbar-title">{{ currentViewTitle }}</div>
        <div class="topbar-spacer"></div>
        <div class="search-box">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input v-model="keyword" placeholder="搜索菜谱..." @keyup.enter="search" />
        </div>
        <div class="topbar-actions">
          <button class="btn btn-primary" @click="openAdd">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            新增菜谱
          </button>
        </div>
      </header>

      <!-- 列表视图 -->
      <div v-if="view === 'list'">
        <div class="toolbar">
          <div class="toolbar-left">
            <span class="result-count">共 <strong>{{ total }}</strong> 道菜谱</span>
            <button v-if="activeFilter !== 'all'" class="filter-chip active" @click="clearFilter">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="12" height="12"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
              {{ getFilterLabel(activeFilter) }}
            </button>
          </div>
          <div class="toolbar-right">
            <select class="sort-select" v-model="sort" @change="fetchRecipes">
              <option value="newest">最新创建</option>
              <option value="oldest">最早创建</option>
              <option value="time_asc">烹饪时间 ↑</option>
              <option value="time_desc">烹饪时间 ↓</option>
              <option value="name">按名称</option>
            </select>
          </div>
        </div>

        <div class="recipe-grid">
          <RecipeCard
            v-for="r in recipes"
            :key="r.id"
            :recipe="r"
            @view="viewDetail"
            @favorite="toggleFavorite"
            @edit="openEdit"
            @delete="confirmDelete"
          />
          <div v-if="!recipes.length" class="empty-state">
            <div class="empty-icon">🍽️</div>
            <h3>暂无菜谱</h3>
            <p>没有找到匹配的菜谱，试试其他关键词或添加新菜谱</p>
            <button class="btn btn-primary" @click="openAdd">+ 新增菜谱</button>
          </div>
        </div>

        <div class="pagination" v-if="totalPages > 1">
          <button :disabled="page === 0" @click="page--; fetchRecipes()">上一页</button>
          <span class="page-info">{{ page + 1 }} / {{ totalPages }}</span>
          <button :disabled="page >= totalPages - 1" @click="page++; fetchRecipes()">下一页</button>
        </div>
      </div>

      <!-- 详情视图 -->
      <RecipeDetail
        v-else-if="view === 'detail'"
        :recipe="currentRecipe"
        @back="view = 'list'"
        @edit="openEdit"
        @favorite="toggleFavorite"
        @delete="onDeleted"
      />

      <!-- 表单 -->
      <RecipeForm
        v-else-if="view === 'form'"
        :recipe="formRecipe"
        @success="(isEdit) => onFormSuccess(isEdit)"
        @cancel="view = 'list'; formRecipe = null"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { recipeAPI } from './api/recipes.js'
import RecipeCard from './components/RecipeCard.vue'
import RecipeDetail from './components/RecipeDetail.vue'
import RecipeForm from './components/RecipeForm.vue'

const view = ref('list')
const recipes = ref([])
const total = ref(0)
const page = ref(0)
const pageSize = 12
const keyword = ref('')
const sort = ref('newest')
const activeFilter = ref('all')
const categories = ref([])
const toasts = ref([])

const totalCount = computed(() => total.value)
const favoritesCount = ref(0)

const totalPages = computed(() => Math.ceil(total.value / pageSize) || 1)

const navItems = computed(() => [
  { key: 'all', label: '全部菜谱', count: totalCount.value, icon: '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>' },
  { key: 'favorites', label: '我的收藏', count: favoritesCount.value, icon: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>' },
])

const currentViewTitle = computed(() => {
  if (view.value === 'detail') return '菜谱详情'
  if (view.value === 'form') return formRecipe.value?.id ? '编辑菜谱' : '新增菜谱'
  const nav = navItems.value.find(i => i.key === activeFilter.value)
  if (nav) return nav.label
  if (activeFilter.value.startsWith('category:')) {
    return activeFilter.value.replace('category:', '')
  }
  return '全部菜谱'
})

function showToast(message, type = 'success') {
  const id = Date.now()
  toasts.value.push({ id, message, type })
  setTimeout(() => {
    toasts.value = toasts.value.filter(t => t.id !== id)
  }, 3000)
}

function setFilter(key) {
  activeFilter.value = key
  page.value = 0
  fetchRecipes()
}

function clearFilter() {
  activeFilter.value = 'all'
  page.value = 0
  fetchRecipes()
}

function getFilterLabel(key) {
  if (key === 'favorites') return '我的收藏'
  if (key.startsWith('category:')) return key.replace('category:', '')
  return key
}

function parseParams() {
  const params = { skip: page.value * pageSize, limit: pageSize, sort: sort.value }
  if (keyword.value) params.keyword = keyword.value
  if (activeFilter.value === 'favorites') params.favorites_only = true
  if (activeFilter.value.startsWith('category:')) params.category = activeFilter.value.replace('category:', '')
  return params
}

async function fetchRecipes() {
  try {
    const res = await recipeAPI.list(parseParams())
    recipes.value = res.data.items
    total.value = res.data.total
  } catch (e) {
    showToast('加载失败', 'error')
  }
}

async function fetchCategories() {
  try {
    const res = await recipeAPI.categories()
    categories.value = res.data.categories
  } catch (e) { /* silent */ }
}

async function fetchFavoritesCount() {
  try {
    const res = await recipeAPI.list({ limit: 1, favorites_only: true })
    favoritesCount.value = res.data.total
  } catch (e) { /* silent */ }
}

const currentRecipe = ref(null)

function viewDetail(id) {
  recipeAPI.get(id).then(r => {
    currentRecipe.value = r.data
    view.value = 'detail'
  })
}

function openEdit(recipe) {
  formRecipe.value = { ...recipe }
  view.value = 'form'
}

function openAdd() {
  formRecipe.value = null
  view.value = 'form'
}

async function toggleFavorite(id) {
  try {
    const res = await recipeAPI.toggleFavorite(id)
    const idx = recipes.value.findIndex(r => r.id === id)
    if (idx !== -1) recipes.value[idx].is_favorite = res.data.is_favorite
    if (currentRecipe.value?.id === id) currentRecipe.value.is_favorite = res.data.is_favorite
    fetchFavoritesCount()
    showToast(res.data.is_favorite ? '已添加到收藏' : '已取消收藏')
  } catch (e) {
    showToast('操作失败', 'error')
  }
}

async function confirmDelete(id) {
  if (!confirm('确定要删除这个菜谱吗？')) return
  try {
    await recipeAPI.delete(id)
    showToast('删除成功')
    fetchRecipes()
    fetchCategories()
    fetchFavoritesCount()
    if (view.value === 'detail') view.value = 'list'
  } catch (e) {
    showToast('删除失败', 'error')
  }
}

function onDeleted() {
  showToast('删除成功')
  view.value = 'list'
  fetchRecipes()
  fetchCategories()
  fetchFavoritesCount()
}

async function onFormSuccess(isEdit) {
  view.value = 'list'
  formRecipe.value = null
  showToast(isEdit ? '修改成功' : '创建成功')
  fetchRecipes()
  fetchCategories()
  fetchFavoritesCount()
}

function search() {
  page.value = 0
  fetchRecipes()
}

onMounted(() => {
  fetchRecipes()
  fetchCategories()
  fetchFavoritesCount()
})
</script>
