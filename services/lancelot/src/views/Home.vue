<template>
  <div class="home">
    <div>
          <video-page></video-page>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {}
})
export default class Home extends Vue {
  options = {
    normalScrollElements: '.video-sidebar',
    dragAndMove: 'fingersonly'
  };
}
</script>

<style scoped lang="scss">
//.video {
//  margin: 0 auto;
//  display: block;
//}

/*.bd-placeholder-img {*/
/*    font-size: 1.125rem;*/
/*    text-anchor: middle;*/
/*    -webkit-user-select: none;*/
/*    -moz-user-select: none;*/
/*    -ms-user-select: none;*/
/*    user-select: none;*/
/*}*/

/*@media (min-width: 768px) {*/
/*    .bd-placeholder-img-lg {*/
/*        font-size: 3.5rem;*/
/*    }*/
/*}*/
</style>
