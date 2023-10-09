import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    server: {
        host: "0.0.0.0",
        port: 3000,
        fs: {
            allow: ['../..'],  // Allow serving files from one level up to the project root
        },
        origin: 'http://localhost:3000',
        hmr: {
            host: '0.0.0.0',
            port: 3000
        },
        watch: {
            usePolling: true,
        },
    },
})
