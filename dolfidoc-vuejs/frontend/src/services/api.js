import axios from 'axios'

// A URL vem automaticamente do .env correto
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default api
