import LoginPage from "@/pages/LoginPage.vue";
import {createRouter, createWebHistory} from "vue-router";
import RequestsManage from "@/pages/RequestsManage.vue";
import Settings from "@/pages/Settings.vue";
import SendRequest from "@/pages/SendRequest.vue";


const routes = [
    {
        path: '/',
        name: 'login',
        component: LoginPage
    },
    {
        path: '/requests',
        name: 'requests',
        component: RequestsManage,
        meta: { requiresAuth: true, allowedRoles: ['staff', 'admin'] }
    },
    {
        path: '/settings',
        name: 'settings',
        component: Settings,
        meta: { requiresAuth: true, allowedRoles: ['admin'] }
    },
    {
        path: '/send-request',
        name: 'send_request',
        component: SendRequest,
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('auth_token');
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next({
        path: '/',
        query: { redirect: to.fullPath } // сохраняем путь для перенаправления после аутентификации
      });
    } else {
      const userRole = localStorage.getItem('user_role'); // Функция, которая получает роль пользователя
      const allowedRoles = to.meta.allowedRoles;
      if (allowedRoles && !allowedRoles.includes(userRole)) {
        // Если пользователь не имеет необходимой роли, перенаправляем его на главную страницу
        next('/');
      } else {
        next();
      }
    }
  } else {
    next();
  }
});

export default router;