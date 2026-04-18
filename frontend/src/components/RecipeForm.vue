<template>
  <div class="form-overlay" @click.self="$emit('cancel')">
    <div class="form-panel">
      <div class="form-header">
        <h2 class="form-title">{{ isEdit ? '编辑菜谱' : '新增菜谱' }}</h2>
        <button class="btn-icon" @click="$emit('cancel')">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>

      <form @submit.prevent="submit">
        <div class="form-group">
          <label>菜谱名称 *</label>
          <input class="form-control" v-model="form.title" required placeholder="例如：红烧肉" />
        </div>

        <div class="form-row">
          <div class="form-group">
            <label>分类 *</label>
            <select class="form-control" v-model="form.category" required>
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
              <option>甜品</option>
              <option>饮品</option>
            </select>
          </div>
          <div class="form-group">
            <label>难度 *</label>
            <select class="form-control" v-model="form.difficulty" required>
              <option value="">请选择</option>
              <option>简单</option>
              <option>中等</option>
              <option>困难</option>
            </select>
          </div>
          <div class="form-group">
            <label>烹饪时间（分钟） *</label>
            <input class="form-control" v-model.number="form.cook_time" type="number" min="1" required placeholder="30" />
          </div>
        </div>

        <div class="form-group">
          <label>图片链接</label>
          <input class="form-control" v-model="form.image_url" placeholder="https://images.unsplash.com/..." />
          <div v-if="form.image_url" style="margin-top:8px;border-radius:8px;overflow:hidden;height:120px;">
            <img :src="form.image_url" style="width:100%;height:100%;object-fit:cover;" @error="form.image_url=''" />
          </div>
        </div>

        <div class="form-group">
          <label>配料（每行一个）</label>
          <textarea class="form-control" v-model="ingredientsText" rows="4" placeholder="鸡蛋 3个&#10;番茄 2个&#10;盐 适量"></textarea>
        </div>

        <div class="form-group">
          <label>烹饪步骤（每行一步）</label>
          <textarea class="form-control" v-model="stepsText" rows="6" placeholder="番茄切块&#10;鸡蛋打散&#10;热油下锅"></textarea>
        </div>

        <div class="form-actions">
          <button type="button" @click="$emit('cancel')" class="btn btn-ghost">取消</button>
          <button type="submit" class="btn btn-primary">{{ isEdit ? '保存修改' : '创建菜谱' }}</button>
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

/**
 * 解析字段为文本行：
 * 优先按 JSON 数组解析，失败则按换行符拆分（兼容纯文本脏数据）
 */
function parseFieldToLines(field) {
  if (!field) return ''
  try {
    const arr = JSON.parse(field)
    if (Array.isArray(arr)) return arr.map(String).join('\n')
  } catch { /* not JSON */ }
  return String(field)
}

const form = ref({
  title: '',
  category: '',
  difficulty: '',
  cook_time: 30,
  image_url: '',
})

const ingredientsText = ref('')
const stepsText = ref('')

watch(() => props.recipe, (r) => {
  if (r) {
    form.value = {
      title: r.title,
      category: r.category,
      difficulty: r.difficulty,
      cook_time: r.cook_time,
      image_url: r.image_url || '',
    }
    ingredientsText.value = parseFieldToLines(r.ingredients)
    stepsText.value = parseFieldToLines(r.steps)
  } else {
    form.value = { title: '', category: '', difficulty: '', cook_time: 30, image_url: '' }
    ingredientsText.value = ''
    stepsText.value = ''
  }
}, { immediate: true })

async function submit() {
  try {
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
    emit('success', isEdit.value)
  } catch (e) {
    alert('保存失败，请检查输入后重试')
  }
}
</script>
