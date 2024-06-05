import { createApp } from 'vue';
import App from './App';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import router from "@/router/router";
import components from "@/components/UI"
import store from "@/store/index";


const cors = require('cors');
const app = createApp(App)

components.forEach(component => {
    app.component(component.name, component)
})

app
    .use(router)
    .use(store)
    // .use(cors())
    .mount('#app')
