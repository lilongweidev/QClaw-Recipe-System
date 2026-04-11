<template>
  <div class="form-overlay">
    <div class="form-panel">
      <h2>{{ isEdit ? '编辑菜谱' : '新增菜谱' }}</h2>
      <form @submit.prevent="submit">
        <div class="form-group">
          <label>菜谱名称 *</label>
          <input v-model="form.title" required placeholder="例如：红烧肉" />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>分类 *</label>
            <select v-model="form.category" required>
              <option value="">请选择</option>
              <option>家常菜</option>
              <option>川菜</option>
              <option>粤菜</option>
              <option>鲁菜</option>
              <option>湘菜</option>
              <option>浙菜</option>
              <option>闽菜</option>
              <option>苏菜</option>
              <option>徽菜</option>
              <option>西餐</option>
              <option>甜点</option>
              <option>饮品</option>
            </select>
          </div>
          <div class="form-group">
            <label>难度 *</label>
            <select v-model="form.difficulty" required>
              <option value="">请选择</option>
              <option>简单</option>
              <option>中等</option>
              <option>困难</option>
            </select>
          </div>
          <div class="form-group">
            <label>烹饪时间（分钟） *</label>
            <input v-model.number="form.cook_time" type="number" min="1" required placeholder="30" />
          </div>
        </div>

        <div class="form-group">
          <label>配料（每行一个）</label>
          <textarea v-model="ingredientsText" rows="4" placeholder="鸡蛋 3个&#10;番茄 2个&#10;盐 适量"></textarea>
        </div>

        <div class="form-group">
          <label>烹饪步骤（每行一步）</label>
          <textarea v-model="stepsText" rows="6" placeholder="番茄切块&#10;鸡蛋打散&#10;热油下锅"></textarea>
        </div>

        <div class="form-actions">
          <button type="button" @click="$emit('cancel')" class="btn-cancel">取消</button>
          <button type="submit" class="btn-submit">{{ isEdit ? '保存修改' : '创建菜谱' }}</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { recipeAPI } from '../api/recipes.js'

const props = defineProps({ recipe: Object })
const emit = defineEmits(['success', 'cancel'])

const isEdit = computed(() => !!props.recipe?.id)

function parseLines(text) {
  return text.split('\n').map(s => s.trim()).filter(Boolean)
}

function linesToText(arr) {
  return Array.isArray(arr) ? arr.join('\n') : ''
}

function parseJsonField(field) {
  try { return JSON.parse(field) } catch { return [] }
}

const form = ref({
  title: '',
  category: '',
  difficulty: '',
  cook_time: 30,
  ingredients: '[]',
  steps: '[]',
})

const ingredientsText = ref('')
const stepsText = ref('')

watch(() => props.recipe, (r) => {
  if (r) {
    form.value = { ...r }
    ingredientsText.value = linesToText(parseJsonField(r.ingredients))
    stepsText.value = linesToText(parseJsonField(r.steps))
  } else {
    form.value = { title: '', category: '', difficulty: '', cook_time: 30, ingredients: '[]', steps: '[]' }
    ingredientsText.value = ''
    stepsText.value = ''
  }
}, { immediate: true })

async function submit() {
  const data = {
    ...form.value,
    ingredients: JSON.stringify(parseLines(ingredientsText.value)),
    steps: JSON.stringify(parseLines(stepsText.value)),
  }
  if (isEdit.value) {
    await recipeAPI.update(props.recipe.id, data)
  } else {
    await recipeAPI.create(data)
  }
  emit('success')
}
</script>
