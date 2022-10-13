<template>
    <div class="login">
        <input type="text" v-model="input_username">
        <input type="password" v-model="input_password">
        <button @click="submitInput">Submit</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    name: 'LoginField',
    data() {
        return{
            input_username: null,
            input_password: null,
            loggedIn: false,
            username: null,
            id: null
        }

    }
    ,
    methods:{
        submitInput: function(){
            const userData = {
                username: this.input_username,
                password: this.input_password
            };

            const path = "http://localhost:8080/login";
            axios.post(path, userData, {
                headers: {
                Accept: "application/json",
                "Content-Type": "application/json;charset=UTF-8",
                },
            })
            .then((res) => {
                const user = res.data;
                if(user.loggedIn){
                    this.loggedIn = true,
                    this.username = user.username,
                    this.id = user.i
                }
            })
            .catch((error) =>{
                console.log(error)
            });
            this.input_username=null;
            this.input_password=null;
        }

    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  </style>
  