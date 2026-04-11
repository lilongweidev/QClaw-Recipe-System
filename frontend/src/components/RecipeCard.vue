<template>
  <div class="recipe-card" @click="$emit('view', recipe.id)">
    <!-- 图片区 -->
    <div class="card-image">
      <img v-if="recipe.image_url" :src="recipe.image_url" :alt="recipe.title" loading="lazy" />
      <div v-else class="card-image-placeholder">🍳</div>
      <button
        class="card-favorite"
        :class="{ favorited: recipe.is_favorite }"
        @click.stop="$emit('favorite', recipe.id)"
        :title="recipe.is_favorite ? '取消收藏' : '添加收藏'"
      >
        <svg viewBox="0 0 24 24" :fill="recipe.is_favorite ? '#e53935' : 'none'" :stroke="recipe.is_favorite ? '#e53935' : '#9ca3af'" stroke-width="2">
          <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
        </svg>
      </button>
    </div>

    <!-- 内容区 -->
    <div class="card-body">
      <div class="card-category">{{ recipe.category }}</div>
      <div class="card-title">{{ recipe.title }}</div>
      <div class="card-meta">
        <span class="card-meta-item">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          {{ recipe.cook_time }} 分钟
        </span>
        <span class="card-difficulty" :class="'difficulty-' + recipe.difficulty">{{ recipe.difficulty }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({ recipe: Object })
defineEmits(['view', 'favorite', 'edit', 'delete'])
</script>
