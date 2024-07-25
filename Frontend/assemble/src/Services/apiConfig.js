import axios from "axios"

const api = axios.create({
    baseURL:
        ProcessingInstruction.env.NODE_env === 'production'
        ? "http://localhost:8000"
        : "http://127.0.0.1:8000",
        headers: {
            'Content-Type': 'application/json'
        }
})

export default api;