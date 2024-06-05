import {createStore} from "vuex";
import {mainModule} from "@/store/mainModule";
import {requestsModule} from "@/store/requestsModule";

export default createStore({
    modules: {
        requests: requestsModule,
        main: mainModule
    }
})