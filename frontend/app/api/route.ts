import axios from 'axios';

async function api(path: string) {
    let url = `http://127.0.0.1:8000/api/${path}`;
    try {
        const res = await axios.get(url);
        return res.data;
    } catch (error) {
        console.error('Erro na requisição:', error);
        throw error;
    }
}

export default api