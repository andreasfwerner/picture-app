<template>
    <div class="login">
        <LoginDiv @onSignIn="signedIn" />
    </div>
</template>

<script>
import LoginDiv from '@/components/LoginField.vue'

export default {
    name: 'LoginView',
    components: {
        LoginDiv
    },
    methods:{
        signedIn(user){
            this.$emit("signedIn",user);
        }
    }
}
</script>