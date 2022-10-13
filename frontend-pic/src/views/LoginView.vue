<template>
    <div class="login">
        <LoginDiv/>
    </div>
</template>

<script>
import LoginDiv from '@/components/LoginField.vue'

export default {
    name: 'LoginView',
    components: {
        LoginDiv
    }
}
</script>