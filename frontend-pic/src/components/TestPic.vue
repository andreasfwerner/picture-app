<template>
    <div class="Test">
        <button @click="getPicture()">Get Pic</button>
        <div class="pic">
            <TestPicProp ref="childComponent"/>
        </div>
    </div>

</template>
  
<script>
import axios from 'axios'
import TestPicProp from './TestPicProp.vue' 


  export default {
    name: 'TestPic',
    
    props:{
        "user_id": Number
    }
    ,
    components:{
        TestPicProp
    }
    ,
    methods:{
        getPicture(){
            const meta = {
                id: this.user_id
            }

            const path = "http://localhost:8080/test"

            axios.post(path,meta)
            .then((res)=>{
                
                const src = `data:image/png;base64,${res.data}`                
                this.$refs.childComponent.updateSrc(src);
            })
            .catch((err)=>{
                console.log(err)
            })


        }
    }
  }
</script>

<style>

    .pic{
        width: 400px;
        height: 400px;
        background-color: blue;
    }
    img{
        width: 200px;
        height: 200px;
    }
</style>
  