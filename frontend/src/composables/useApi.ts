import axios from "axios";
const urlPrefix = 'http://localhost:8000/api';

export default function () {
    return {
        get: async (url: string, params: any = {}) => { // TODO generic type for params mby
            const response = await axios.get(urlPrefix + url, { params });
            // @ts-ignore
            return response.data;
            },
        post: (url: string, data: any) => {
            return axios.post(urlPrefix + url, data);
        },
        patch: (url: string, data: any) => {
            return axios.patch(urlPrefix + url, data);
        },
        delete: (url: string) => {
            return axios.delete(urlPrefix + url);
        },
    }
}

