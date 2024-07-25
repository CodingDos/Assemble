import {useState} from 'react'
import axios from 'axios';
import Button from '../../Components/Form/Button';

function Auth() {
    return (
        <>
            <Register />
            <Login />
        </>
    )
}

function Register(){
    const [formData, setFormData] = useState({
        email:'',
        username: '',
        password: ''
    });

    const handleChange = (e) => {
        const {name,value} = e.target;

        setFormData((prev) => ({
            ...prev,
            [name] : value
        }))
    };
    
    const registerUser =  async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/users/', formData)
            console.log(response)
        } catch (error){
            console.error("Error creating a User", error)
        }
    };
    
    return (
        <div>
            <h1>Register</h1>
            <form action={registerUser}>
                <label htmlFor='email'>Email: </label>
                <input 
                    name='email' 
                    type='text'
                    value={formData.email} 
                    onChange={handleChange}
                    placeholder="email@example.com"
                    // required
                />
                <hr />
                <label htmlFor='username'>Username: </label>
                <input 
                    name='username'
                    type='text'
                    value={formData.username}
                    onChange={handleChange}
                    // required
                />
                <hr />
                <label htmlFor='password'>Password: </label>
                <input 
                    name='password'  
                    type='password'
                    value={formData.password}
                    onChange={handleChange}
                    placeholder="*******"
                />
                <Button pendingMessage='...Submitting' message='Submit'/>
            </form>
        </div>
    )
}

function Login(){
    const [formData, setFormData] = useState({
        email:'',
        password:'',
    })

    const handleChange = (e) => {
        const {name, value} = e.target;

        setFormData((prev) => ({
            ...prev,
            [name]: value
        }))
    }

    const signIn = async(e) => {
        e.preventDefault()
        try {
            const response = await axios.post('/users/')
            console.log(response)
        } catch (error) {
            console.error("Error trying to login: ", error)
        }
    }

    return (
        <div>
            <h1>Login</h1>
            <form action={signIn}>
                <label htmlFor='username'>Username: </label>
                    <input 
                        name='username'  
                        type='text'
                        value={formData.username}
                        onChange={handleChange}
                    />
                <br />
                <label htmlFor='password'>Password: </label>
                    <input 
                        name='password'  
                        type='password'
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="*******"
                    />
                <Button pendingMessage='...Submitting' message='Submit'/>
            </form>
        </div>
    )
}


export default Auth

