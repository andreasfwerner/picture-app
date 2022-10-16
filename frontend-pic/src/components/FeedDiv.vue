<template>
    <div class="FeedDiv" >
        <FeedPicture ref="childComponent"
                    :date_posted="dates[curr]"
                    :name="names[curr]"
                    :description="descs[curr]"
                    :pic_src="pics[curr]"
                    >
        </FeedPicture>
    </div>
</template>
  
  <script>
  import FeedPicture from './FeedPicture.vue'
  import axios from 'axios'

  export default {
    name: 'FeedDiv',
    components: {
        FeedPicture,
    },
    props:{
      user_id: Number,
      curr: Number
    }
    ,
    data(){
        return{
            pics:[],
            names:[],
            dates:[],
            descs:[],
        }
    },
    methods:{
        getPicture(){
            const meta = {
                id: this.user_id
            }

            const path = "http://localhost:8080/test"

            axios.post(path,meta)
            .then((res)=>{
                for(let i=0; i<res.data.pic_list.length;i++){
                    const src = `data:image/png;base64,${res.data.pic_list[i]}`
                    this.pics.push(src)
                    this.descs.push(res.data.desc_list[i])
                    this.names.push(res.data.name_list[i])
                    this.dates.push(res.data.date_list[i])
                    this.$emit('initPic',this.pics.length)
                }
                setTimeout(() => {
                        this.$refs.childComponent.updateSrc();
                },"200") 
               
            })
            .catch((err)=>{
                console.log(err)
            })
        },
        updatePic(){
            setTimeout(() => {
                    this.$refs.childComponent.updateSrc();
                },"200") 
            
        }
        

    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  .FeedDiv{
    width: 100%;
    height: 80%;
    background-color: black;
  }
  
  </style>
  