export const sendRequestModule = {
    state: () => ({
        requestAddressId: -1,
        requestApartmentNumber: -1
    }),
    getters: {},
    mutations: {
        setRequestAddressId(state, pk) {
            state.requestAddressId = pk
        },
        setRequestApartmentNumber(state, number) {
            state.requestApartmentNumber = number
        }
    },
    actions: {},
    namespaced: true
}