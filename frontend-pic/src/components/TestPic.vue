<template>
    <div class="Test">
        <button @click="getPicture()">Get Pic</button>
        <div class="pic" v-for="pic in pics">
            <TestPicProp ref="childComponent" :pic_src="pic"/>
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
            pics:[]
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
                console.log(res)
                for(let i=0; i<res.data.result.length;i++){
                    const src = `data:image/png;base64,${res.data.result[i]}`
                    this.pics.push(src)
                }
                setTimeout(() => {
                    for(let i=0; i<this.pics.length;i++){
                        this.$refs.childComponent[i].updateSrc();
                        console.log(i)
                    }
                    
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
  