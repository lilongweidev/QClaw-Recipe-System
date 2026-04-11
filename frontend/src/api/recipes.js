import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
})

export const recipeAPI = {
  // 获取菜谱列表
  list(params = {}) {
    return api.get('/recipes', { params })
  },
  // 获取单个菜谱
  get(id) {
    return api.get(`/recipes/${id}`)
  },
  // 新增菜谱
  create(data) {
    return api.post('/recipes', data)
  },
  // 更新菜谱
  update(id, data) {
    return api.put(`/recipes/${id}`, data)
  },
  // 删除菜谱
  delete(id) {
    return api.delete(`/recipes/${id}`)
  },
}
