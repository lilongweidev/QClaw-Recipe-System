<template>
  <div class="detail-view" v-if="recipe">
    <button class="detail-back" @click="$emit('back')">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" width="14" height="14"><polyline points="15 18 9 12 15 6"/></svg>
      返回列表
    </button>

    <!-- Hero -->
    <div class="detail-hero">
      <img v-if="recipe.image_url" :src="recipe.image_url" :alt="recipe.title" />
      <div v-else class="detail-hero-placeholder">🍳</div>
    </div>

    <!-- 基本信息 -->
    <div class="detail-badges">
      <span class="detail-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
        {{ recipe.category }}
      </span>
      <span class="detail-badge">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
        {{ recipe.cook_time }} 分钟
      </span>
      <span class="detail-badge card-difficulty" :class="'difficulty-' + recipe.difficulty">
        {{ recipe.difficulty }}
      </span>
      <button
        class="detail-badge"
        style="border:none;cursor:pointer;font-family:var(--font);"
        :style="{ background: recipe.is_favorite ? '#fff0f0' : 'white' }"
        @click="$emit('favorite', recipe.id)"
      >
        <svg viewBox="0 0 24 24" :fill="recipe.is_favorite ? '#e53935' : 'none'" :stroke="recipe.is_favorite ? '#e53935' : 'currentColor'" stroke-width="2" width="14" height="14">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
        </svg>
        {{ recipe.is_favorite ? '已收藏' : '添加收藏' }}
      </button>
    </div>

    <!-- 配料 -->
    <div class="detail-section">
      <div class="detail-section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        所需配料
      </div>
      <div class="ingredient-grid">
        <div v-for="(item, i) in ingredients" :key="i" class="ingredient-item">{{ item }}</div>
      </div>
    </div>

    <!-- 步骤 -->
    <div class="detail-section">
      <div class="detail-section-title">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
        烹饪步骤
      </div>
      <ol class="step-list">
        <li v-for="(step, i) in steps" :key="i" class="step-item">
          <span class="step-number">{{ i + 1 }}</span>
          <span class="step-text">{{ step }}</span>
        </li>
      </ol>
    </div>

    <!-- 操作按钮 -->
    <div class="detail-section" style="display:flex;gap:10px;justify-content:flex-end;">
      <button class="btn btn-ghost" @click="$emit('edit', recipe)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
        编辑菜谱
      </button>
      <button class="btn btn-ghost" style="color:#e53935;" @click="$emit('delete', recipe.id)">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14H6L5 6"/><path d="M10 11v6M14 11v6"/><path d="M9 6V4h6v2"/></svg>
        删除
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({ recipe: Object })
defineEmits(['back', 'edit', 'favorite', 'delete'])

function parseJsonField(field) {
  try { return JSON.parse(field) } catch { return [] }
}

const ingredients = computed(() => parseJsonField(props.recipe?.ingredients))
const steps = computed(() => parseJsonField(props.recipe?.steps))
</script>
