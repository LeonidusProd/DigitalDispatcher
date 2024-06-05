import {createStore} from "vuex";
import {mainModule} from "@/store/mainModule";
import {requestsModule} from "@/store/requestsModule";
import {sendRequestModule} from "@/store/sendRequestModule";

export default createStore({
    modules: {
        requests: requestsModule,
        main: mainModule,
        sendRequest: sendRequestModule
    }
})