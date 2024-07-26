import api from "./apiConfig.js"

//Users Section

export const getUsers = async () => {
    try {
        const response = await api.get('/users/')
        return response.data
    } catch (error) {
        throw error
    }
}

export const getOneUser = async (id) => {
    try {
        const response = await api.get(`/users/${id}/`)
        return response.data
    } catch (error) {
        throw error
    }
}

export const signOut = async () => {
    try {
        let sessionInfo = sessionStorage.getItem(session)
        if(sessionInfo){
            sessionStorage.removeItem(key, value)
        } else {
            throw error
        }
    } catch (error) {
        throw error
    }
}

export const signIn = async (username, password) => {
    try {
        
    } catch (error) {
        
    }
}

//Hackathon Section

export const getHackathons = async () => {
    try {
        const response = await api.get('/hackathons/')
        return response.data
    } catch (error) {
        throw error
    }
}

export const getOneHackathon = async (id) => {
    try {
        const response = await api.get(`/hackathons/${id}`)
        return response.data
    } catch (error) {
       throw error 
    }
}

//Teams section

export const getTeams = async () => {
    try {
        const response = await api.get('/teams/')
        return response.data
    } catch (error) {
        throw error
    }
}

export const getOneTeam = async (id) => {
    try {
        const response = await api.get(`/teams/${id}`)
        return response.data
    } catch (error) {
        throw error
    }
}

//Skills section

export const getSkills = async () => {
    try {
        const response = await api.get('/skills/')
        return response.data
    } catch (error) {
        throw error
    }
}

