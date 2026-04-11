<template>
  <div class="detail-panel" v-if="recipe">
    <div class="detail-header">
      <button class="btn-back" @click="$emit('back')">← 返回列表</button>
      <div class="header-actions">
        <button @click="$emit('edit', recipe)">编辑</button>
        <button @click="confirmDelete" class="btn-delete">删除</button>
      </div>
    </div>

    <div class="detail-body">
      <div class="detail-meta">
        <span class="tag">{{ recipe.category }}</span>
        <span class="difficulty" :class="recipe.difficulty">{{ recipe.difficulty }}</span>
        <span class="cook-time">⏱ {{ recipe.cook_time }} 分钟</span>
      </div>

      <h1 class="detail-title">{{ recipe.title }}</h1>

      <div class="section">
        <h2>🥗 配料</h2>
        <ul class="ingredient-list">
          <li v-for="(item, i) in ingredients" :key="i">{{ item }}</li>
        </ul>
      </div>

      <div class="section">
        <h2>👨‍🍳 烹饪步骤</h2>
        <ol class="step-list">
          <li v-for="(step, i) in steps" :key="i">
            <span class="step-num">{{ i + 1 }}</span>
            <span>{{ step }}</span>
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { recipeAPI } from '../api/recipes.js'

const props = defineProps({ recipe: Object })
const emit = defineEmits(['back', 'edit'])

function parseJsonField(field) {
  try { return JSON.parse(field) } catch { return [] }
}

const ingredients = computed(() => parseJsonField(props.recipe?.ingredients))
const steps = computed(() => parseJsonField(props.recipe?.steps))

async function confirmDelete() {
  if (!confirm('确定要删除这个菜谱吗？')) return
  await recipeAPI.delete(props.recipe.id)
  emit('back')
}
</script>
