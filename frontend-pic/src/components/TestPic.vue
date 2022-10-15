<template>
    <div class="Test">
        <button @click="getPicture()">Get Pic</button>
        <div class="pic">
            <TestPicProp ref="childComponent" :pic_src="pic_src"/>
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

    data(){
        return{
            pic_src:null
        }
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
                this.pic_src = src
                console.log(this.pic_src)
                setTimeout(() => {
                    this.$refs.childComponent.updateSrc();
                },"500") 
               
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
</style>
  