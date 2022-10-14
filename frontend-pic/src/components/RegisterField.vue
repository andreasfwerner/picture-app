<template>
    <div class="register">
        <input type="text" v-model="input_username">
        <input type="password" v-model="input_password">
        <input type="password" v-model="password_verification">
        <div class="FileUploadButton">
            <input name="file" id="file" class="FileUploadInput inputfile" type="file" @change="onFileSelect" >
            <label for="file">SELECT IMAGE</label>
        </div>
        <button @click="submitRegisterInput">Submit</button>
        <p v-if="!password_checker">Password Doesnt Match</p>
        <p v-if="!username_unique">USERNAME TAKEN</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios'

  export default {
    name: 'RegisterField',
    data() {
        return{
            input_username: null,
            input_password: null,
            password_verification: null,
            password_checker: false,
            username: null,
            username_unique: true,
            selectedFile: null,
        }

    }
    ,
    methods:{
        onFileSelect(event){
            this.selectedFile = event.target.files[0]
        },
        submitRegisterInput: function(){
            if(this.input_password==this.password_verification && this.input_password.length>3){


            const fd = new FormData();
            fd.append('image',this.selectedFile)
            fd.append('username',this.input_username);
            fd.append('password',this.input_password);


            const path = "http://localhost:8080/register";
            
            axios.post(path,fd)
            .then((res) => {
                const meta = res.data;
                if(!meta.unique){
                    this.username_unique = false;
                }
            })
            .catch((error) =>{
                console.log(error)
            })
            ;

            this.input_password = null
            this.input_username = null
            this.password_verification = null

        }
        else{
            this.input_password = null
            this.input_username = null
            this.password_verification = null
        }
    },
  }}
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>

  </style>
  