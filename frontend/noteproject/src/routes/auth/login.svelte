<script lang="ts">
	import '../../app.css';
</script>

<svelte:head>
	<title>Login--Notium</title>
</svelte:head>

<div class="flex items-center justify-center min-h-screen bg-secondary text-primary">
	<div class="px-8 py-6 mt-4 text-left bg-secondary shadow-lg">
		<div class="flex justify-center">
			<svg
				width="145"
				height="48"
				viewBox="0 0 145 48"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					fill-rule="evenodd"
					clip-rule="evenodd"
					d="M7 14C7 11.2386 9.23858 9 12 9H32C34.7614 9 37 11.2386 37 14V24.9795L22.9795 39H12C9.23858 39 7 36.7614 7 34V14ZM28.0132 39L37 30.0132V34C37 36.7614 34.7614 39 32 39H28.0132ZM14.6271 19.1694C16.0312 19.1694 17.1694 18.0312 17.1694 16.6271C17.1694 15.223 16.0312 14.0847 14.6271 14.0847C13.223 14.0847 12.0847 15.223 12.0847 16.6271C12.0847 18.0312 13.223 19.1694 14.6271 19.1694ZM17.1694 24.2542C17.1694 25.6583 16.0312 26.7966 14.6271 26.7966C13.223 26.7966 12.0847 25.6583 12.0847 24.2542C12.0847 22.8501 13.223 21.7118 14.6271 21.7118C16.0312 21.7118 17.1694 22.8501 17.1694 24.2542ZM14.6271 34.4237C16.0312 34.4237 17.1694 33.2855 17.1694 31.8814C17.1694 30.4772 16.0312 29.339 14.6271 29.339C13.223 29.339 12.0847 30.4772 12.0847 31.8814C12.0847 33.2855 13.223 34.4237 14.6271 34.4237ZM19.2034 16.6271C19.2034 16.0655 19.6587 15.6102 20.2203 15.6102H31.4068C31.9684 15.6102 32.4237 16.0655 32.4237 16.6271C32.4237 17.1888 31.9684 17.6441 31.4068 17.6441H20.2203C19.6587 17.6441 19.2034 17.1888 19.2034 16.6271ZM20.2203 23.2373C19.6587 23.2373 19.2034 23.6926 19.2034 24.2542C19.2034 24.8159 19.6587 25.2712 20.2203 25.2712H28.3559C28.9176 25.2712 29.3729 24.8159 29.3729 24.2542C29.3729 23.6926 28.9176 23.2373 28.3559 23.2373H20.2203Z"
					fill="#FF6400"
				/>
				<path
					d="M49.92 32.2C48.8667 32.2 48.06 31.9 47.5 31.3C46.9533 30.7 46.68 29.8533 46.68 28.76V21.24C46.68 20.1467 46.9533 19.3 47.5 18.7C48.06 18.1 48.8667 17.8 49.92 17.8C50.9733 17.8 51.7733 18.1 52.32 18.7C52.88 19.3 53.16 20.1467 53.16 21.24V22.72H51.08V21.1C51.08 20.2333 50.7133 19.8 49.98 19.8C49.2467 19.8 48.88 20.2333 48.88 21.1V28.92C48.88 29.7733 49.2467 30.2 49.98 30.2C50.7133 30.2 51.08 29.7733 51.08 28.92V26.78H53.16V28.76C53.16 29.8533 52.88 30.7 52.32 31.3C51.7733 31.9 50.9733 32.2 49.92 32.2ZM65.6763 32.2C64.6096 32.2 63.7963 31.9 63.2363 31.3C62.6763 30.6867 62.3963 29.8133 62.3963 28.68V18H64.5962V28.84C64.5962 29.32 64.6896 29.6667 64.8763 29.88C65.0763 30.0933 65.3563 30.2 65.7163 30.2C66.0763 30.2 66.3496 30.0933 66.5363 29.88C66.7363 29.6667 66.8363 29.32 66.8363 28.84V18H68.9563V28.68C68.9563 29.8133 68.6763 30.6867 68.1163 31.3C67.5563 31.9 66.7429 32.2 65.6763 32.2ZM80.2431 20H77.9431V18H84.7431V20H82.4431V32H80.2431V20ZM96.9102 32.2C95.8302 32.2 95.0035 31.8933 94.4302 31.28C93.8568 30.6667 93.5702 29.8 93.5702 28.68V21.32C93.5702 20.2 93.8568 19.3333 94.4302 18.72C95.0035 18.1067 95.8302 17.8 96.9102 17.8C97.9902 17.8 98.8168 18.1067 99.3902 18.72C99.9635 19.3333 100.25 20.2 100.25 21.32V28.68C100.25 29.8 99.9635 30.6667 99.3902 31.28C98.8168 31.8933 97.9902 32.2 96.9102 32.2ZM96.9102 30.2C97.6702 30.2 98.0502 29.74 98.0502 28.82V21.18C98.0502 20.26 97.6702 19.8 96.9102 19.8C96.1502 19.8 95.7702 20.26 95.7702 21.18V28.82C95.7702 29.74 96.1502 30.2 96.9102 30.2ZM109.738 18H113.098C114.191 18 115.011 18.2933 115.558 18.88C116.105 19.4667 116.378 20.3267 116.378 21.46V28.54C116.378 29.6733 116.105 30.5333 115.558 31.12C115.011 31.7067 114.191 32 113.098 32H109.738V18ZM113.058 30C113.418 30 113.691 29.8933 113.878 29.68C114.078 29.4667 114.178 29.12 114.178 28.64V21.36C114.178 20.88 114.078 20.5333 113.878 20.32C113.691 20.1067 113.418 20 113.058 20H111.938V30H113.058ZM129.043 32.2C127.963 32.2 127.136 31.8933 126.563 31.28C125.99 30.6667 125.703 29.8 125.703 28.68V21.32C125.703 20.2 125.99 19.3333 126.563 18.72C127.136 18.1067 127.963 17.8 129.043 17.8C130.123 17.8 130.95 18.1067 131.523 18.72C132.096 19.3333 132.383 20.2 132.383 21.32V28.68C132.383 29.8 132.096 30.6667 131.523 31.28C130.95 31.8933 130.123 32.2 129.043 32.2ZM129.043 30.2C129.803 30.2 130.183 29.74 130.183 28.82V21.18C130.183 20.26 129.803 19.8 129.043 19.8C128.283 19.8 127.903 20.26 127.903 21.18V28.82C127.903 29.74 128.283 30.2 129.043 30.2Z"
					fill="#FF6400"
				/>
			</svg>
		</div>
		<h3 class="text-sm font-bold text-center">Login to your account</h3>
		<form>
			<div class="mt-4">
				<div>
					<label class="block" for="email"
						>Email<label>
							<input
								type="text"
								placeholder="Email"
								class="shadow-md todo w-full px-4 py-2 mt-2 input input-ghost border rounded-md focus:outline-none focus:ring-1 focus:ring-primary bg-secondary"
							/>
							<span class="text-xs tracking-wide text-primary">Email field is required </span>
						</label></label
					>
				</div>
				<!-- class="input todo input-ghost text-primary bg-secondary" -->
				<div class="mt-4">
					<!-- svelte-ignore a11y-label-has-associated-control -->
					<label class="block"
						>Password<label>
							<input
								type="password"
								placeholder="Password"
								class="shadow-md todo w-full px-4 py-2 mt-2 input input-ghost border rounded-md focus:outline-none focus:ring-1 focus:ring-primary bg-secondary"
							/>
						</label></label
					>
				</div>
				<div class="flex items-baseline justify-between">
					<button
						type="submit"
						formaction="/"
						class="px-6 py-2 mt-4 text-secondary bg-primary rounded-lg font-bold"
					>
						Login</button
					>

					<!-- svelte-ignore a11y-invalid-attribute -->
					<a href="/" class="text-sm text-primary hover:underline">Forgot password?</a>
				</div>
				<a href="/auth/register" class="text-xs text-primary hover:underline"
					>New user ? Register NOW!</a
				>
			</div>
		</form>
	</div>
</div>

<!-- <div class="hero min-h-screen bg-base-200">

<div class="flex-col justify-center hero-content lg:flex-row">

<div class="text-center lg:text-left">

<h1 class="mb-5 text-5xl font-bold">Hello there</h1>

<p class="mb-5">A todo list manager for your life.</p>

</div>

<div class="card flex-shrink-0 w-full max-w-sm shadow-2xl bg-base-100">

<div class="card-body">

<div class="form-control">

<label class="label">

<span class="label-text">Email</span>

</label>

<input type="text" placeholder="email" class="input input-bordered" />

</div>

<div class="form-control">

<label class="label">

<span class="label-text">Password</span>

</label>

<input type="text" placeholder="password" class="input input-bordered" />

<label class="label">

<a href="#" class="label-text-alt">Forgot password?</a>

</label>

</div>

<div class="form-control mt-6">

<input type="button" value="Login" class="btn btn-primary" />

</div>

</div>

</div>

</div>
    </div> -->
<style>
	.todo {
		color: #ff6400;
	}
</style>
