<template>
    <div class="login">
        <div class="row justify-content-center h-100">
            <form class="form-signin col-3 align-middle">
                <img class="mb-4" src="https://getbootstrap.com/docs/4.0/assets/brand/bootstrap-solid.svg" alt=""
                     width="72" height="72">
                <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
                <label for="inputEmail" class="sr-only">Email address</label>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required=""
                       autofocus="" data-keeper-lock-id="k-j0h2m7ayf0f">
                <label for="inputPassword" class="sr-only">Password</label>
                <input type="password" id="inputPassword" class="form-control" placeholder="Password" required=""
                       data-keeper-lock-id="k-p0z2lkb807">
                <div class="checkbox mb-3">
                    <label>
                        <input type="checkbox" value="remember-me"> Remember me
                    </label>
                </div>
                <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
                <p class="mt-5 mb-3 text-muted">© 2017-2018</p>
            </form>
        </div>
    </div>
</template>

<script lang="ts">
	import {Component, Vue} from "vue-property-decorator";

	@Component({
		components: {}
	})
	export default class Login extends Vue {
	}
</script>
<style>
    .form-signin{
        padding: 20px;
        border: 1px solid #2c3e50;
        border-radius: 20px;
    }
</style>

