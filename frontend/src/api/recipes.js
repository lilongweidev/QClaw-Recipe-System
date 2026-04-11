import axios from 'axios'

const BASE = '/api'

const client = axios.create({
  baseURL: BASE,
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

export const recipeAPI = {
  list(params = {}) {
    return client.get('/recipes', { params })
  },

  get(id) {
    return client.get(`/recipes/${id}`)
  },

  create(data) {
    return client.post('/recipes', data)
  },

  update(id, data) {
    return client.put(`/recipes/${id}`, data)
  },

  delete(id) {
    return client.delete(`/recipes/${id}`)
  },

  toggleFavorite(id) {
    return client.patch(`/recipes/${id}/favorite`)
  },

  categories() {
    return client.get('/recipes/categories')
  },
}
