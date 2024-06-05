export const requestsModule = {
    state: () => ({
        activeRequestId: -1
    }),
    getters: {},
    mutations: {
        setActiveRequestId(state, pk) {
            state.activeRequestId = pk
        }
    },
    actions: {},
    namespaced: true
}