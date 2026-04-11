<template>
  <div id="app">
    <header class="app-header">
      <h1>🍳 QClaw 菜谱管理系统</h1>
      <nav>
        <span v-if="view === 'list'" class="nav-hint">共 {{ total }} 道菜谱</span>
      </nav>
    </header>

    <main class="app-main">
      <!-- 列表视图 -->
      <RecipeList
        v-if="view === 'list'"
        @view="viewDetail"
        @edit="openEdit"
        @add="openAdd"
      />

      <!-- 详情视图 -->
      <RecipeDetail
        v-else-if="view === 'detail'"
        :recipe="currentRecipe"
        @back="view = 'list'; currentRecipe = null"
        @edit="openEdit"
      />

      <!-- 新增/编辑表单 -->
      <RecipeForm
        v-else-if="view === 'form'"
        :recipe="formRecipe"
        @success="onFormSuccess"
        @cancel="view = 'list'; formRecipe = null"
      />
    </main>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import RecipeList from './components/RecipeList.vue'
import RecipeDetail from './components/RecipeDetail.vue'
import RecipeForm from './components/RecipeForm.vue'
import { recipeAPI } from './api/recipes.js'

const view = ref('list')
const currentRecipe = ref(null)
const formRecipe = ref(null)
const total = ref(0)

async function viewDetail(id) {
  const res = await recipeAPI.get(id)
  currentRecipe.value = res.data
  view.value = 'detail'
}

function openEdit(recipe) {
  formRecipe.value = { ...recipe }
  view.value = 'form'
}

function openAdd() {
  formRecipe.value = null
  view.value = 'form'
}

async function onFormSuccess() {
  view.value = 'list'
  formRecipe.value = null
}
</script>
