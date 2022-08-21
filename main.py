from bs4 import BeautifulSoup
import re

response = '''
<!DOCTYPE html>
<html lang="en">

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Area codes locator - Area code lookup by number or city</title>
	<meta name="description"
		content="Area code lookup for US cities and an area codes locator to find the location of area codes. Complete area code list for the US and Canada">
	<meta name="format-detection" content="telephone=no">


	<link rel="stylesheet" href="/automin/7d82ee75bfc5544844822fb1d0401acb2d9eca45.automin.cache_extend.1660602886.css"
		type="text/css">

	<!-- Responsive Ad code here since it isn't supported in external stylesheets -->
	<style>
		.ad-unit {
			display: inline-block;
			margin: 0;
		}

		.ad-unit-parent {
			text-align: center;
			display: block;
			overflow-x: hidden;
			margin: 0;
		}

		.xs-120x240 {
			width: 120px;
			height: 240px;
		}

		.xs-200x200 {
			width: 200px;
			height: 200px;
		}

		.xs-250x250 {
			width: 250px;
			height: 250px;
		}

		.xs-300x250 {
			width: 300px;
			height: 250px;
		}

		.xs-336x280 {
			width: 300px;
			height: 250px;
		}

		@media (min-width: 336px) {
			.xs-336x280 {
				width: 336px;
				height: 280px;
			}
		}

		.xs-320x50 {
			width: 320px;
			height: 50px;
		}

		.xs-320x100 {
			width: 320px;
			height: 100px;
		}


		/* xs only */
		@media (max-width: 767px) {
			.ad-unit {
				margin: 5px 0;
			}

			.ad-unit-parent {
				margin-left: -15px;
				margin-right: -15px;
			}
		}

		/* sm */
		@media (min-width: 768px) {
			.ad-unit-parent {
				overflow-x: visible;
			}

			.sm-728x90 {
				width: 728px;
				height: 90px;
			}

			.sm-468x60 {
				width: 468px;
				height: 60px;
			}

			.sm-160x600 {
				width: 160px;
				height: 600px;
			}

			.sm-120x240 {
				width: 120px;
				height: 240px;
			}

			.sm-200x200 {
				width: 200px;
				height: 200px;
			}

			.sm-250x250 {
				width: 250px;
				height: 250px;
			}

			.sm-300x250 {
				width: 300px;
				height: 250px;
			}

			.sm-336x280 {
				width: 336px;
				height: 280px;
			}

			.sm-300x600 {
				width: 300px;
				height: 600px;
			}

			.sm-320x50 {
				width: 320px;
				height: 50px;
			}

			.sm-320x100 {
				width: 320px;
				height: 100px;
			}
		}

		/* md */
		@media (min-width: 992px) {
			.md-728x90 {
				width: 728px;
				height: 90px;
			}

			.md-468x60 {
				width: 468px;
				height: 60px;
			}

			.md-160x600 {
				width: 160px;
				height: 600px;
			}

			.md-120x240 {
				width: 120px;
				height: 240px;
			}

			.md-200x200 {
				width: 200px;
				height: 200px;
			}

			.md-250x250 {
				width: 250px;
				height: 250px;
			}

			.md-300x250 {
				width: 300px;
				height: 250px;
			}

			.md-336x280 {
				width: 336px;
				height: 280px;
			}

			.md-300x600 {
				width: 300px;
				height: 600px;
			}

			.md-320x50 {
				width: 320px;
				height: 50px;
			}

			.md-320x100 {
				width: 320px;
				height: 100px;
			}
		}

		/* lg */
		@media (min-width: 1200px) {
			.lg-728x90 {
				width: 728px;
				height: 90px;
			}

			.lg-468x60 {
				width: 468px;
				height: 60px;
			}

			.lg-160x600 {
				width: 160px;
				height: 600px;
			}

			.lg-120x240 {
				width: 120px;
				height: 240px;
			}

			.lg-200x200 {
				width: 200px;
				height: 200px;
			}

			.lg-250x250 {
				width: 250px;
				height: 250px;
			}

			.lg-300x250 {
				width: 300px;
				height: 250px;
			}

			.lg-336x280 {
				width: 336px;
				height: 280px;
			}

			.lg-300x600 {
				width: 300px;
				height: 600px;
			}

			.lg-320x50 {
				width: 320px;
				height: 50px;
			}

			.lg-320x100 {
				width: 320px;
				height: 100px;
			}

			.lg-970x90 {
				width: 970px;
				height: 90px;
			}

			.lg-970x250 {
				width: 970px;
				height: 250px;
			}
		}

		/* sm */
		@media(min-width:768px) {
			.top-ad-container {
				float: right;
				margin: 15px;
			}

			.bottom-ad-container {
				float: left;
				margin: 15px;
			}
		}
	</style>
	<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

	<meta property="og:title" content="AllAreaCodes: Lookup area codes and phone numbers" />
	<meta property="og:site_name" content="AllAreaCodes" />
	<meta property="og:url" content="https://www.allareacodes.com/" />
	<meta property="og:description"
		content="Area code lookup by number or city, maps, reverse phone lookup, and international calling." />
	<meta property="og:type" content="website" />
	<style>
		#lookup FORM {
			display: none;
		}

		#lookup {
			display: none;
		}

		#top {
			overflow: hidden;
		}

		H1 {
			margin: 0 0 15px 0;
		}

		.bg_div {
			background: url(/images/home-bg3.cache_extend.1660602886.jpg);
			background-size: cover;
			margin: 0 -15px;
			padding: 25px 15px;
			border-top: 3px solid #133558;
			border-bottom: 3px solid #133558;

			text-shadow: 1px 1px 3px #000000;
			color: #FFFFFF;
			text-align: center;
			font-size: 20px;
		}

		.bg_div .box {
			box-shadow: 2px 2px 5px 0px rgba(0, 0, 0, 0.5);
		}

		.codes_column {
			position: relative;
			min-height: 1px;
			float: left;
			width: 12.5%;
			font-size: 11px;
		}
	</style>
	<style>
		.D3ChartOuterContainer {
			max-width: 1200px;
		}

		.D3ChartContainer {
			position: relative;
			width: 100%;
			margin: 0 auto;
			padding-bottom: 70%;
			height: 0;
		}

		@media(min-width:768px) {
			.D3ChartContainer {
				padding-bottom: 40%;
			}
		}

		.D3SizingContainer {
			position: absolute;
			left: 0;
			width: 100%;
			height: 100%;
		}

		/* tag names are case-sensitive in IE and FF */
		.D3ChartContainer svg {
			width: 100%;
			height: 100%;
		}
	</style>
	<link href="//cdnjs.cloudflare.com/ajax/libs/nvd3/1.8.1/nv.d3.min.css" rel="stylesheet" crossorigin="anonymous" />
	<style>
		.NVD3ChartIcon {
			font-family: FontAwesome;
			font-size: 18px;
			fill: #CCCCCC;
			visibility: hidden;
		}

		.NVD3ChartIcon:HOVER {
			fill: #000000;
			cursor: pointer;
		}

		@media(min-width:768px) {
			.NVD3ChartIcon {
				visibility: visible;
			}
		}

		.NVD3ChartFooter {
			font-size: 11px;
			font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
		}

		.NVD3ChartFooter A {
			text-decoration: underline;
		}
	</style>
	<style>
		.LineChart .nv-point {
			fill-opacity: 1 !important;
		}

		.LineChart.subtle-points .nv-point {
			fill-opacity: 0.5 !important;
		}

		.LineChart.sparkline .nv-point {
			fill-opacity: 0 !important;
		}

		.LineChart.sparkline .NVD3ChartIcon {
			visibility: hidden;
		}

		.LineChart.LineChartHideDots .nv-point {
			fill-opacity: 0 !important;
		}
	</style>
	<style>
		.TableBarChartRow {
			padding: 10px;
			background-color: #f6f6f6;
			position: relative;
			margin: 2px 0;
		}

		.TableBarChartBg {
			display: inline-block;
			height: 100%;
			top: 0;
			left: 0;
			position: absolute;
			z-index: 0;
			opacity: 0.6;
		}

		.TableBarChartText {
			display: flex;
			position: relative;
			z-index: 1;
		}

		.TableBarChartLabel {
			white-space: nowrap;
			overflow: hidden;
			text-overflow: ellipsis;
			flex-grow: 1;
		}

		.TableBarChartValue {
			white-space: nowrap;
		}
	</style>
</head>

<body>

	<div class="container">

		<!-- Static navbar -->
		<div class="navbar navbar-default" role="navigation" id="small-nav">
			<div class="container-fluid">
				<div class="navbar-header">
					<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
					<a class="navbar-brand" href="#">
						<img src="/images/new/aac_logo.cache_extend.1660602886.jpg" class="img-responsive" alt="Logo">
				</a>
				</div>
				<div class="navbar-collapse collapse">
					<ul class="nav navbar-nav">
						<li><a href="/">Home</a></li>
						<li><a href="/area-code-list.htm">Area Code List</a></li>
						<li><a href="/reverse-phone-lookup/">Reverse Phone Lookup</a></li>
						<li><a href="/area-code-lookup/">Area Code Lookup</a></li>
						<li><a href="/area-code-map.htm"">Area Code Map</a></li>
					<li><a href="/canadian_area_codes.htm"">Canada Area Codes List</a> </li> </ul> </div> <!--/.nav-collapse -->
				</div>
				<!--/.container-fluid -->
			</div>


			<div class="row">
				<div class="col-xs-12" id="top">

					<img src="/images/new/globe.cache_extend.1660602886.png" alt="Globe" id="globe"/>

					<a href="/"><img src="/images/new/large-logo.cache_extend.1660602886.gif" alt="Logo" id="logo"/></a>

						<ul class="links">
							<li><a href="/">Home</a></li>
							<li><a href="/area-code-list.htm">Area Code List</a></li>
							<li><a href="/reverse-phone-lookup/">Reverse Phone Lookup</a></li>
							<li><a href="/area-code-lookup/">Area Code Lookup</a></li>
							<li><a href="/area-code-map.htm"">Area Code Map</a></li>
				<li><a href="/canadian_area_codes.htm"">Canada Area Codes List</a> </li> </ul> </div> <div class="col-xs-12"
									id="lookup">
									<form action="/reverse-phone-lookup/" method="post">

										<img src="/images/new/phone.cache_extend.1660602886.png" alt="Phone"/>

										<div class="clearfix">
											<span>Instant Phone Lookup</span>
											<input type="text" name="q" tabindex="1" value="" class="form-control" type="text"><button type="submit" class="btn btn-danger" tabindex="2">Search</button>

											<p>Enter a phone number, area code, or city and state.</p>
										</div>


									</form>
				</div>
			</div>

			<div class="row">
				<div class="col-xs-12">
					<div class="bg_div">
						<h1>Phone and Area Code Search</h1>

						<script>
							function homeSearchValidation() {
			if ($('#home_q').val() == '') {
				if ($('#home_q').attr('placeholder') == '(555) 555-5555') {
					alert('Please enter a phone number');
				} else {
					$('#home_q').val($('#home_q').attr('placeholder'));
				}
			}
		}
						</script>
						Search by:<br>
						<form action="/reverse-phone-lookup/" method="post" onsubmit="homeSearchValidation();">
							<div class="btn-group btn-group-lg" data-toggle="buttons">
								<label class="btn btn-primary active" onclick="$('#home_q').attr('placeholder', '(555) 555-5555');">
				<input type="radio" name="search_type" id="option1" autocomplete="off" checked> Phone
			</label>
								<label class="btn btn-primary" onclick="$('#home_q').attr('placeholder', '');">
				<input type="radio" name="search_type" id="option2" autocomplete="off"> Area Code
			</label>
								<label class="btn btn-primary" onclick="$('#home_q').attr('placeholder', '');">
				<input type="radio" name="search_type" id="option3" autocomplete="off"> City
			</label>
							</div>

							<div class="input-group input-group-lg" style="max-width: 350px; margin: 10px auto">
								<input type="text" name="q" id="home_q" class="form-control" placeholder="(555) 555-5555"/>
								<span class="input-group-btn">
				<button type="submit" class="btn btn-danger">Search</button>
			</span>
							</div>
						</form>
					</div>

					<div class="row">
						<div class="col-xs-12"
							style="padding-top: 15px; padding-bottom: 15px; background-color: #eee; border-bottom: 3px solid #133558">
							<div style="font-size: 22px; text-align: center; font-weight: bold" class="featured-in">
								Featured In
								<div class="row">
									<div class="col-xs-6 col-sm-4 col-md-2 "
										style="margin-top: 8px; margin-bottom: 8px">
										<img src="/shared-assets/featured-logos/forbes.cache_extend.1638201401.png" alt="Forbes Logo" class="img-responsive center-block">
					</div>
										<div class="col-xs-6 col-sm-4 col-md-2 "
											style="margin-top: 8px; margin-bottom: 8px">
											<img src="/shared-assets/featured-logos/gizmodo.cache_extend.1638201401.png" alt="Gizmodo Logo" class="img-responsive center-block">
					</div>
											<div class="col-xs-6 col-sm-4 col-md-2 "
												style="margin-top: 8px; margin-bottom: 8px">
												<img src="/shared-assets/featured-logos/cnn.cache_extend.1638201401.png" alt="CNN Logo" class="img-responsive center-block">
					</div>
												<div class="col-xs-6 col-sm-4 col-md-2 "
													style="margin-top: 8px; margin-bottom: 8px">
													<img src="/shared-assets/featured-logos/msn.cache_extend.1638201401.png" alt="MSN Logo" class="img-responsive center-block">
					</div>
													<div class="col-xs-6 col-sm-4 col-md-2 "
														style="margin-top: 8px; margin-bottom: 8px">
														<img src="/shared-assets/featured-logos/business-insider.cache_extend.1638201401.png" alt="Business Insider Logo" class="img-responsive center-block">
					</div>
														<div class="col-xs-6 col-sm-4 col-md-2 "
															style="margin-top: 8px; margin-bottom: 8px">
															<img src="/shared-assets/featured-logos/pcmag.cache_extend.1638201401.png" alt="PCMag Logo" class="img-responsive center-block">
					</div>
														</div>
													</div>
												</div>
											</div>

											<div class="row" style="text-align: center">
												<div class="col-md-6">
													<h2><a href="/area-code-map.htm">US Area Code Map</a></h2>
													<a href="/area-code-map.htm"><img src="/maps/us-area-code-map-thumb.png" class="img-responsive" alt="area code map"></a><br>
	</div>
														<div class="col-md-6">
															<h2><a href="/canadian_area_codes.htm">Canada Area Code
																	Map</a></h2>
															<a href="/canadian_area_codes.htm"><img src="/maps/canada-area-code-map-thumb.png" class="img-responsive" alt="canada area code map"></a><br>
	</div>
														</div>

														<div class="row">
															<div class="col-md-4">
																<h2>By Number</h2>
																<table cellpadding=0 cellspacing=0 border=0
																	id="area-codes-table">
																	<tr>
																		<td align=right valign=top
																			style="padding-top: 8px; line-height: 20px; width: 52px">
																			<a href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_2').show(); return false;"
																				id="codes_2_selector"
																				class="div_selector_active">200s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_3').show(); return false;"
																				id="codes_3_selector"
																				class="div_selector_inactive">300s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_4').show(); return false;"
																				id="codes_4_selector"
																				class="div_selector_inactive">400s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_5').show(); return false;"
																				id="codes_5_selector"
																				class="div_selector_inactive">500s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_6').show(); return false;"
																				id="codes_6_selector"
																				class="div_selector_inactive">600s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_7').show(); return false;"
																				id="codes_7_selector"
																				class="div_selector_inactive">700s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_8').show(); return false;"
																				id="codes_8_selector"
																				class="div_selector_inactive">800s</a><br><a
																				href="#"
																				onclick="$('.div_selector_active').removeClass('div_selector_active').addClass('div_selector_inactive'); $(this).removeClass('div_selector_inactive').addClass('div_selector_active'); $('.codes_container').hide(); $('#codes_9').show(); return false;"
																				id="codes_9_selector"
																				class="div_selector_inactive">900s</a><br></td>
																		<td
																			style="background-color: #F2F3F7; padding: 8px; line-height: 20px">
																			<div id="codes_2" class="codes_container"><a
																					href="/201"><b>201</b> - Jersey
																					City, NJ</a><br><a
																					href="/202"><b>202</b> - District of
																					Columbia</a><br><a
																					href="/203"><b>203</b> - Bridgeport,
																					CT</a><br><a href="/204"><b>204</b>
																					- Manitoba</a><br><a
																					href="/205"><b>205</b> - Birmingham,
																					AL</a><br><a href="/206"><b>206</b>
																					- Seattle, WA</a><br><a
																					href="/207"><b>207</b> - Portland,
																					ME</a><br><a href="/208"><b>208</b>
																					- Idaho</a><br><a
																					href="/209"><b>209</b> - Stockton,
																					CA</a><br><a href="/210"><b>210</b>
																					- San Antonio, TX</a><br><a
																					href="/212"><b>212</b> - New York,
																					NY</a><br><a href="/213"><b>213</b>
																					- Los Angeles, CA</a><br><a
																					href="/214"><b>214</b> - Dallas,
																					TX</a><br><a href="/215"><b>215</b>
																					- Philadelphia, PA</a><br><a
																					href="/216"><b>216</b> - Cleveland,
																					OH</a><br><a href="/217"><b>217</b>
																					- Springfield, IL</a><br><a
																					href="/218"><b>218</b> - Duluth,
																					MN</a><br><a href="/219"><b>219</b>
																					- Hammond, IN</a><br><a
																					href="/220"><b>220</b> - Newark,
																					OH</a><br><a href="/223"><b>223</b>
																					- Lancaster, PA</a><br><a
																					href="/224"><b>224</b> - Elgin,
																					IL</a><br><a href="/225"><b>225</b>
																					- Baton Rouge, LA</a><br><a
																					href="/226"><b>226</b> - London,
																					ON</a><br><a href="/228"><b>228</b>
																					- Gulfport, MS</a><br><a
																					href="/229"><b>229</b> - Albany,
																					GA</a><br><a href="/231"><b>231</b>
																					- Muskegon, MI</a><br><a
																					href="/234"><b>234</b> - Akron,
																					OH</a><br><a href="/236"><b>236</b>
																					- Vancouver, BC</a><br><a
																					href="/239"><b>239</b> - Cape Coral,
																					FL</a><br><a href="/240"><b>240</b>
																					- Germantown, MD</a><br><a
																					href="/248"><b>248</b> - Troy,
																					MI</a><br><a href="/249"><b>249</b>
																					- Sudbury, ON</a><br><a
																					href="/250"><b>250</b> - Kelowna,
																					BC</a><br><a href="/251"><b>251</b>
																					- Mobile, AL</a><br><a
																					href="/252"><b>252</b> - Greenville,
																					NC</a><br><a href="/253"><b>253</b>
																					- Tacoma, WA</a><br><a
																					href="/254"><b>254</b> - Killeen,
																					TX</a><br><a href="/256"><b>256</b>
																					- Huntsville, AL</a><br><a
																					href="/260"><b>260</b> - Fort Wayne,
																					IN</a><br><a href="/262"><b>262</b>
																					- Kenosha, WI</a><br><a
																					href="/267"><b>267</b> -
																					Philadelphia, PA</a><br><a
																					href="/269"><b>269</b> - Kalamazoo,
																					MI</a><br><a href="/270"><b>270</b>
																					- Bowling Green, KY</a><br><a
																					href="/272"><b>272</b> - Scranton,
																					PA</a><br><a href="/276"><b>276</b>
																					- Bristol, VA</a><br><a
																					href="/279"><b>279</b> - Sacramento,
																					CA</a><br><a href="/281"><b>281</b>
																					- Houston, TX</a><br><a
																					href="/289"><b>289</b> - Hamilton,
																					ON</a><br></div>
																				<div id="codes_3"
																					class="codes_container"><a
																						href="/301"><b>301</b> -
																						Germantown, MD</a><br><a
																						href="/302"><b>302</b> -
																						Delaware</a><br><a
																						href="/303"><b>303</b> - Denver,
																						CO</a><br><a
																						href="/304"><b>304</b> - West
																						Virginia</a><br><a
																						href="/305"><b>305</b> - Miami,
																						FL</a><br><a
																						href="/306"><b>306</b> -
																						Saskatchewan</a><br><a
																						href="/307"><b>307</b> -
																						Wyoming</a><br><a
																						href="/308"><b>308</b> - Grand
																						Island, NE</a><br><a
																						href="/309"><b>309</b> - Peoria,
																						IL</a><br><a
																						href="/310"><b>310</b> - Los
																						Angeles, CA</a><br><a
																						href="/312"><b>312</b> -
																						Chicago, IL</a><br><a
																						href="/313"><b>313</b> -
																						Detroit, MI</a><br><a
																						href="/314"><b>314</b> - St.
																						Louis, MO</a><br><a
																						href="/315"><b>315</b> -
																						Syracuse, NY</a><br><a
																						href="/316"><b>316</b> -
																						Wichita, KS</a><br><a
																						href="/317"><b>317</b> -
																						Indianapolis, IN</a><br><a
																						href="/318"><b>318</b> -
																						Shreveport, LA</a><br><a
																						href="/319"><b>319</b> - Cedar
																						Rapids, IA</a><br><a
																						href="/320"><b>320</b> - St.
																						Cloud, MN</a><br><a
																						href="/321"><b>321</b> -
																						Orlando, FL</a><br><a
																						href="/323"><b>323</b> - Los
																						Angeles, CA</a><br><a
																						href="/325"><b>325</b> -
																						Abilene, TX</a><br><a
																						href="/330"><b>330</b> - Akron,
																						OH</a><br><a
																						href="/331"><b>331</b> - Aurora,
																						IL</a><br><a
																						href="/332"><b>332</b> - New
																						York, NY</a><br><a
																						href="/334"><b>334</b> -
																						Montgomery, AL</a><br><a
																						href="/336"><b>336</b> -
																						Greensboro, NC</a><br><a
																						href="/337"><b>337</b> -
																						Lafayette, LA</a><br><a
																						href="/339"><b>339</b> - Boston,
																						MA</a><br><a
																						href="/340"><b>340</b> - Virgin
																						Islands</a><br><a
																						href="/343"><b>343</b> - Ottawa,
																						ON</a><br><a
																						href="/346"><b>346</b> -
																						Houston, TX</a><br><a
																						href="/347"><b>347</b> - New
																						York, NY</a><br><a
																						href="/351"><b>351</b> - Lowell,
																						MA</a><br><a
																						href="/352"><b>352</b> -
																						Gainesville, FL</a><br><a
																						href="/360"><b>360</b> -
																						Vancouver, WA</a><br><a
																						href="/361"><b>361</b> - Corpus
																						Christi, TX</a><br><a
																						href="/364"><b>364</b> - Bowling
																						Green, KY</a><br><a
																						href="/365"><b>365</b> -
																						Hamilton, ON</a><br><a
																						href="/367"><b>367</b> - Quebec,
																						QC</a><br><a
																						href="/380"><b>380</b> -
																						Columbus, OH</a><br><a
																						href="/385"><b>385</b> - Salt
																						Lake City, UT</a><br><a
																						href="/386"><b>386</b> - Palm
																						Coast, FL</a><br></div>
																					<div id="codes_4"
																						class="codes_container"><a
																							href="/401"><b>401</b> -
																							Providence, RI</a><br><a
																							href="/402"><b>402</b> -
																							Omaha, NE</a><br><a
																							href="/403"><b>403</b> -
																							Calgary, AB</a><br><a
																							href="/404"><b>404</b> -
																							Atlanta, GA</a><br><a
																							href="/405"><b>405</b> -
																							Oklahoma City, OK</a><br><a
																							href="/406"><b>406</b> -
																							Montana</a><br><a
																							href="/407"><b>407</b> -
																							Orlando, FL</a><br><a
																							href="/408"><b>408</b> - San
																							Jose, CA</a><br><a
																							href="/409"><b>409</b> -
																							Beaumont, TX</a><br><a
																							href="/410"><b>410</b> -
																							Baltimore, MD</a><br><a
																							href="/412"><b>412</b> -
																							Pittsburgh, PA</a><br><a
																							href="/413"><b>413</b> -
																							Springfield, MA</a><br><a
																							href="/414"><b>414</b> -
																							Milwaukee, WI</a><br><a
																							href="/415"><b>415</b> - San
																							Francisco, CA</a><br><a
																							href="/416"><b>416</b> -
																							Toronto, ON</a><br><a
																							href="/417"><b>417</b> -
																							Springfield, MO</a><br><a
																							href="/418"><b>418</b> -
																							Quebec, QC</a><br><a
																							href="/419"><b>419</b> -
																							Toledo, OH</a><br><a
																							href="/423"><b>423</b> -
																							Chattanooga, TN</a><br><a
																							href="/424"><b>424</b> - Los
																							Angeles, CA</a><br><a
																							href="/425"><b>425</b> -
																							Bellevue, WA</a><br><a
																							href="/430"><b>430</b> -
																							Tyler, TX</a><br><a
																							href="/431"><b>431</b> -
																							Manitoba</a><br><a
																							href="/432"><b>432</b> -
																							Midland, TX</a><br><a
																							href="/434"><b>434</b> -
																							Lynchburg, VA</a><br><a
																							href="/435"><b>435</b> - St.
																							George, UT</a><br><a
																							href="/437"><b>437</b> -
																							Toronto, ON</a><br><a
																							href="/438"><b>438</b> -
																							Montreal, QC</a><br><a
																							href="/440"><b>440</b> -
																							Parma, OH</a><br><a
																							href="/442"><b>442</b> -
																							Oceanside, CA</a><br><a
																							href="/443"><b>443</b> -
																							Baltimore, MD</a><br><a
																							href="/445"><b>445</b> -
																							Philadelphia, PA</a><br><a
																							href="/450"><b>450</b> -
																							Granby, QC</a><br><a
																							href="/458"><b>458</b> -
																							Eugene, OR</a><br><a
																							href="/463"><b>463</b> -
																							Indianapolis, IN</a><br><a
																							href="/469"><b>469</b> -
																							Dallas, TX</a><br><a
																							href="/470"><b>470</b> -
																							Atlanta, GA</a><br><a
																							href="/475"><b>475</b> -
																							Bridgeport, CT</a><br><a
																							href="/478"><b>478</b> -
																							Macon, GA</a><br><a
																							href="/479"><b>479</b> -
																							Fort Smith, AR</a><br><a
																							href="/480"><b>480</b> -
																							Mesa, AZ</a><br><a
																							href="/484"><b>484</b> -
																							Allentown, PA</a><br></div>
																						<div id="codes_5"
																							class="codes_container"><a
																								href="/501"><b>501</b> -
																								Little Rock,
																								AR</a><br><a
																								href="/502"><b>502</b> -
																								Louisville, KY</a><br><a
																								href="/503"><b>503</b> -
																								Portland, OR</a><br><a
																								href="/504"><b>504</b> -
																								New Orleans,
																								LA</a><br><a
																								href="/505"><b>505</b> -
																								Albuquerque,
																								NM</a><br><a
																								href="/506"><b>506</b> -
																								New Brunswick</a><br><a
																								href="/507"><b>507</b> -
																								Rochester, MN</a><br><a
																								href="/508"><b>508</b> -
																								Worcester, MA</a><br><a
																								href="/509"><b>509</b> -
																								Spokane, WA</a><br><a
																								href="/510"><b>510</b> -
																								Oakland, CA</a><br><a
																								href="/512"><b>512</b> -
																								Austin, TX</a><br><a
																								href="/513"><b>513</b> -
																								Cincinnati, OH</a><br><a
																								href="/514"><b>514</b> -
																								Montreal, QC</a><br><a
																								href="/515"><b>515</b> -
																								Des Moines, IA</a><br><a
																								href="/516"><b>516</b> -
																								Hempstead, NY</a><br><a
																								href="/517"><b>517</b> -
																								Lansing, MI</a><br><a
																								href="/518"><b>518</b> -
																								Albany, NY</a><br><a
																								href="/519"><b>519</b> -
																								London, ON</a><br><a
																								href="/520"><b>520</b> -
																								Tucson, AZ</a><br><a
																								href="/530"><b>530</b> -
																								Redding, CA</a><br><a
																								href="/531"><b>531</b> -
																								Omaha, NE</a><br><a
																								href="/534"><b>534</b> -
																								Eau Claire, WI</a><br><a
																								href="/539"><b>539</b> -
																								Tulsa, OK</a><br><a
																								href="/540"><b>540</b> -
																								Roanoke, VA</a><br><a
																								href="/541"><b>541</b> -
																								Eugene, OR</a><br><a
																								href="/548"><b>548</b> -
																								London, ON</a><br><a
																								href="/551"><b>551</b> -
																								Jersey City,
																								NJ</a><br><a
																								href="/559"><b>559</b> -
																								Fresno, CA</a><br><a
																								href="/561"><b>561</b> -
																								West Palm Beach,
																								FL</a><br><a
																								href="/562"><b>562</b> -
																								Long Beach, CA</a><br><a
																								href="/563"><b>563</b> -
																								Davenport, IA</a><br><a
																								href="/564"><b>564</b> -
																								Vancouver, WA</a><br><a
																								href="/567"><b>567</b> -
																								Toledo, OH</a><br><a
																								href="/570"><b>570</b> -
																								Scranton, PA</a><br><a
																								href="/571"><b>571</b> -
																								Arlington, VA</a><br><a
																								href="/573"><b>573</b> -
																								Columbia, MO</a><br><a
																								href="/574"><b>574</b> -
																								South Bend, IN</a><br><a
																								href="/575"><b>575</b> -
																								Las Cruces, NM</a><br><a
																								href="/579"><b>579</b> -
																								Granby, QC</a><br><a
																								href="/580"><b>580</b> -
																								Lawton, OK</a><br><a
																								href="/581"><b>581</b> -
																								Quebec, QC</a><br><a
																								href="/585"><b>585</b> -
																								Rochester, NY</a><br><a
																								href="/586"><b>586</b> -
																								Warren, MI</a><br><a
																								href="/587"><b>587</b> -
																								Calgary,
																								AB</a><br></div>
																							<div id="codes_6"
																								class="codes_container">
																								<a href="/601"><b>601</b>
																									- Jackson,
																									MS</a><br><a
																									href="/602"><b>602</b>
																									- Phoenix,
																									AZ</a><br><a
																									href="/603"><b>603</b>
																									- New
																									Hampshire</a><br><a
																									href="/604"><b>604</b>
																									- Vancouver,
																									BC</a><br><a
																									href="/605"><b>605</b>
																									- South
																									Dakota</a><br><a
																									href="/606"><b>606</b>
																									- Ashland,
																									KY</a><br><a
																									href="/607"><b>607</b>
																									- Binghamton,
																									NY</a><br><a
																									href="/608"><b>608</b>
																									- Madison,
																									WI</a><br><a
																									href="/609"><b>609</b>
																									- Trenton,
																									NJ</a><br><a
																									href="/610"><b>610</b>
																									- Allentown,
																									PA</a><br><a
																									href="/612"><b>612</b>
																									- Minneapolis,
																									MN</a><br><a
																									href="/613"><b>613</b>
																									- Ottawa,
																									ON</a><br><a
																									href="/614"><b>614</b>
																									- Columbus,
																									OH</a><br><a
																									href="/615"><b>615</b>
																									- Nashville,
																									TN</a><br><a
																									href="/616"><b>616</b>
																									- Grand Rapids,
																									MI</a><br><a
																									href="/617"><b>617</b>
																									- Boston,
																									MA</a><br><a
																									href="/618"><b>618</b>
																									- Belleville,
																									IL</a><br><a
																									href="/619"><b>619</b>
																									- San Diego,
																									CA</a><br><a
																									href="/620"><b>620</b>
																									- Hutchinson,
																									KS</a><br><a
																									href="/623"><b>623</b>
																									- Phoenix,
																									AZ</a><br><a
																									href="/626"><b>626</b>
																									- Pasadena,
																									CA</a><br><a
																									href="/628"><b>628</b>
																									- San Francisco,
																									CA</a><br><a
																									href="/629"><b>629</b>
																									- Nashville,
																									TN</a><br><a
																									href="/630"><b>630</b>
																									- Aurora,
																									IL</a><br><a
																									href="/631"><b>631</b>
																									- Brentwood,
																									NY</a><br><a
																									href="/636"><b>636</b>
																									- O'Fallon,
																									MO</a><br><a
																									href="/639"><b>639</b>
																									-
																									Saskatchewan</a><br><a
																									href="/640"><b>640</b>
																									- Trenton,
																									NJ</a><br><a
																									href="/641"><b>641</b>
																									- Mason City,
																									IA</a><br><a
																									href="/646"><b>646</b>
																									- New York,
																									NY</a><br><a
																									href="/647"><b>647</b>
																									- Toronto,
																									ON</a><br><a
																									href="/650"><b>650</b>
																									- San Mateo,
																									CA</a><br><a
																									href="/651"><b>651</b>
																									- St. Paul,
																									MN</a><br><a
																									href="/657"><b>657</b>
																									- Anaheim,
																									CA</a><br><a
																									href="/660"><b>660</b>
																									- Sedalia,
																									MO</a><br><a
																									href="/661"><b>661</b>
																									- Bakersfield,
																									CA</a><br><a
																									href="/662"><b>662</b>
																									- Southaven,
																									MS</a><br><a
																									href="/667"><b>667</b>
																									- Baltimore,
																									MD</a><br><a
																									href="/669"><b>669</b>
																									- San Jose,
																									CA</a><br><a
																									href="/670"><b>670</b>
																									- Northern Mariana
																									Islands</a><br><a
																									href="/671"><b>671</b>
																									- Guam</a><br><a
																									href="/678"><b>678</b>
																									- Atlanta,
																									GA</a><br><a
																									href="/680"><b>680</b>
																									- Syracuse,
																									NY</a><br><a
																									href="/681"><b>681</b>
																									- West
																									Virginia</a><br><a
																									href="/682"><b>682</b>
																									- Fort Worth,
																									TX</a><br><a
																									href="/684"><b>684</b>
																									- American
																									Samoa</a><br></div>
																								<div id="codes_7"
																									class="codes_container">
																									<a href="/701"><b>701</b>
																										- North
																										Dakota</a><br><a
																										href="/702"><b>702</b>
																										- Las Vegas,
																										NV</a><br><a
																										href="/703"><b>703</b>
																										- Arlington,
																										VA</a><br><a
																										href="/704"><b>704</b>
																										- Charlotte,
																										NC</a><br><a
																										href="/705"><b>705</b>
																										- Sudbury,
																										ON</a><br><a
																										href="/706"><b>706</b>
																										- Augusta,
																										GA</a><br><a
																										href="/707"><b>707</b>
																										- Santa Rosa,
																										CA</a><br><a
																										href="/708"><b>708</b>
																										- Cicero,
																										IL</a><br><a
																										href="/709"><b>709</b>
																										-
																										Newfoundland/Labrador</a><br><a
																										href="/712"><b>712</b>
																										- Sioux City,
																										IA</a><br><a
																										href="/713"><b>713</b>
																										- Houston,
																										TX</a><br><a
																										href="/714"><b>714</b>
																										- Anaheim,
																										CA</a><br><a
																										href="/715"><b>715</b>
																										- Eau Claire,
																										WI</a><br><a
																										href="/716"><b>716</b>
																										- Buffalo,
																										NY</a><br><a
																										href="/717"><b>717</b>
																										- Lancaster,
																										PA</a><br><a
																										href="/718"><b>718</b>
																										- New York,
																										NY</a><br><a
																										href="/719"><b>719</b>
																										- Colorado
																										Springs,
																										CO</a><br><a
																										href="/720"><b>720</b>
																										- Denver,
																										CO</a><br><a
																										href="/724"><b>724</b>
																										- New Castle,
																										PA</a><br><a
																										href="/725"><b>725</b>
																										- Las Vegas,
																										NV</a><br><a
																										href="/726"><b>726</b>
																										- San Antonio,
																										TX</a><br><a
																										href="/727"><b>727</b>
																										- St.
																										Petersburg,
																										FL</a><br><a
																										href="/731"><b>731</b>
																										- Jackson,
																										TN</a><br><a
																										href="/732"><b>732</b>
																										- Toms River,
																										NJ</a><br><a
																										href="/734"><b>734</b>
																										- Ann Arbor,
																										MI</a><br><a
																										href="/737"><b>737</b>
																										- Austin,
																										TX</a><br><a
																										href="/740"><b>740</b>
																										- Newark,
																										OH</a><br><a
																										href="/743"><b>743</b>
																										- Greensboro,
																										NC</a><br><a
																										href="/747"><b>747</b>
																										- Los Angeles,
																										CA</a><br><a
																										href="/754"><b>754</b>
																										- Fort
																										Lauderdale,
																										FL</a><br><a
																										href="/757"><b>757</b>
																										- Virginia
																										Beach,
																										VA</a><br><a
																										href="/760"><b>760</b>
																										- Oceanside,
																										CA</a><br><a
																										href="/762"><b>762</b>
																										- Augusta,
																										GA</a><br><a
																										href="/763"><b>763</b>
																										- Brooklyn Park,
																										MN</a><br><a
																										href="/765"><b>765</b>
																										- Muncie,
																										IN</a><br><a
																										href="/769"><b>769</b>
																										- Jackson,
																										MS</a><br><a
																										href="/770"><b>770</b>
																										- Roswell,
																										GA</a><br><a
																										href="/772"><b>772</b>
																										- Port St.
																										Lucie,
																										FL</a><br><a
																										href="/773"><b>773</b>
																										- Chicago,
																										IL</a><br><a
																										href="/774"><b>774</b>
																										- Worcester,
																										MA</a><br><a
																										href="/775"><b>775</b>
																										- Reno,
																										NV</a><br><a
																										href="/778"><b>778</b>
																										- Vancouver,
																										BC</a><br><a
																										href="/779"><b>779</b>
																										- Rockford,
																										IL</a><br><a
																										href="/780"><b>780</b>
																										- Edmonton,
																										AB</a><br><a
																										href="/781"><b>781</b>
																										- Boston,
																										MA</a><br><a
																										href="/782"><b>782</b>
																										- Nova Scotia/PE
																										Island</a><br><a
																										href="/785"><b>785</b>
																										- Topeka,
																										KS</a><br><a
																										href="/786"><b>786</b>
																										- Miami,
																										FL</a><br><a
																										href="/787"><b>787</b>
																										- Puerto
																										Rico</a><br></div>
																									<div id="codes_8"
																										class="codes_container">
																										<a href="/801"><b>801</b>
																											- Salt Lake
																											City,
																											UT</a><br><a
																											href="/802"><b>802</b>
																											-
																											Vermont</a><br><a
																											href="/803"><b>803</b>
																											- Columbia,
																											SC</a><br><a
																											href="/804"><b>804</b>
																											- Richmond,
																											VA</a><br><a
																											href="/805"><b>805</b>
																											- Oxnard,
																											CA</a><br><a
																											href="/806"><b>806</b>
																											- Lubbock,
																											TX</a><br><a
																											href="/807"><b>807</b>
																											- Kenora,
																											ON</a><br><a
																											href="/808"><b>808</b>
																											-
																											Hawaii</a><br><a
																											href="/810"><b>810</b>
																											- Flint,
																											MI</a><br><a
																											href="/812"><b>812</b>
																											-
																											Evansville,
																											IN</a><br><a
																											href="/813"><b>813</b>
																											- Tampa,
																											FL</a><br><a
																											href="/814"><b>814</b>
																											- Erie,
																											PA</a><br><a
																											href="/815"><b>815</b>
																											- Rockford,
																											IL</a><br><a
																											href="/816"><b>816</b>
																											- Kansas
																											City,
																											MO</a><br><a
																											href="/817"><b>817</b>
																											- Fort
																											Worth,
																											TX</a><br><a
																											href="/818"><b>818</b>
																											- Los
																											Angeles,
																											CA</a><br><a
																											href="/819"><b>819</b>
																											-
																											Sherbrooke,
																											QC</a><br><a
																											href="/820"><b>820</b>
																											- Oxnard,
																											CA</a><br><a
																											href="/825"><b>825</b>
																											- Calgary,
																											AB</a><br><a
																											href="/828"><b>828</b>
																											- Asheville,
																											NC</a><br><a
																											href="/830"><b>830</b>
																											- New
																											Braunfels,
																											TX</a><br><a
																											href="/831"><b>831</b>
																											- Salinas,
																											CA</a><br><a
																											href="/832"><b>832</b>
																											- Houston,
																											TX</a><br><a
																											href="/838"><b>838</b>
																											- Albany,
																											NY</a><br><a
																											href="/843"><b>843</b>
																											-
																											Charleston,
																											SC</a><br><a
																											href="/845"><b>845</b>
																											- New City,
																											NY</a><br><a
																											href="/847"><b>847</b>
																											- Elgin,
																											IL</a><br><a
																											href="/848"><b>848</b>
																											- Toms
																											River,
																											NJ</a><br><a
																											href="/850"><b>850</b>
																											-
																											Tallahassee,
																											FL</a><br><a
																											href="/854"><b>854</b>
																											-
																											Charleston,
																											SC</a><br><a
																											href="/856"><b>856</b>
																											- Camden,
																											NJ</a><br><a
																											href="/857"><b>857</b>
																											- Boston,
																											MA</a><br><a
																											href="/858"><b>858</b>
																											- San Diego,
																											CA</a><br><a
																											href="/859"><b>859</b>
																											-
																											Lexington-Fayette,
																											KY</a><br><a
																											href="/860"><b>860</b>
																											- Hartford,
																											CT</a><br><a
																											href="/862"><b>862</b>
																											- Newark,
																											NJ</a><br><a
																											href="/863"><b>863</b>
																											- Lakeland,
																											FL</a><br><a
																											href="/864"><b>864</b>
																											-
																											Greenville,
																											SC</a><br><a
																											href="/865"><b>865</b>
																											- Knoxville,
																											TN</a><br><a
																											href="/867"><b>867</b>
																											- Northern
																											Canada</a><br><a
																											href="/870"><b>870</b>
																											- Jonesboro,
																											AR</a><br><a
																											href="/872"><b>872</b>
																											- Chicago,
																											IL</a><br><a
																											href="/873"><b>873</b>
																											-
																											Sherbrooke,
																											QC</a><br><a
																											href="/878"><b>878</b>
																											-
																											Pittsburgh,
																											PA</a><br></div>
																										<div id="codes_9"
																											class="codes_container">
																											<a
																												href="/901"><b>901</b>
																												-
																												Memphis,
																												TN</a><br><a
																												href="/902"><b>902</b>
																												- Nova
																												Scotia/PE
																												Island</a><br><a
																												href="/903"><b>903</b>
																												- Tyler,
																												TX</a><br><a
																												href="/904"><b>904</b>
																												-
																												Jacksonville,
																												FL</a><br><a
																												href="/905"><b>905</b>
																												-
																												Hamilton,
																												ON</a><br><a
																												href="/906"><b>906</b>
																												-
																												Marquette,
																												MI</a><br><a
																												href="/907"><b>907</b>
																												-
																												Alaska</a><br><a
																												href="/908"><b>908</b>
																												-
																												Elizabeth,
																												NJ</a><br><a
																												href="/909"><b>909</b>
																												- San
																												Bernardino,
																												CA</a><br><a
																												href="/910"><b>910</b>
																												-
																												Fayetteville,
																												NC</a><br><a
																												href="/912"><b>912</b>
																												-
																												Savannah,
																												GA</a><br><a
																												href="/913"><b>913</b>
																												-
																												Overland
																												Park,
																												KS</a><br><a
																												href="/914"><b>914</b>
																												-
																												Yonkers,
																												NY</a><br><a
																												href="/915"><b>915</b>
																												- El
																												Paso,
																												TX</a><br><a
																												href="/916"><b>916</b>
																												-
																												Sacramento,
																												CA</a><br><a
																												href="/917"><b>917</b>
																												- New
																												York,
																												NY</a><br><a
																												href="/918"><b>918</b>
																												- Tulsa,
																												OK</a><br><a
																												href="/919"><b>919</b>
																												-
																												Raleigh,
																												NC</a><br><a
																												href="/920"><b>920</b>
																												- Green
																												Bay,
																												WI</a><br><a
																												href="/925"><b>925</b>
																												-
																												Concord,
																												CA</a><br><a
																												href="/928"><b>928</b>
																												- Yuma,
																												AZ</a><br><a
																												href="/929"><b>929</b>
																												- New
																												York,
																												NY</a><br><a
																												href="/930"><b>930</b>
																												-
																												Evansville,
																												IN</a><br><a
																												href="/931"><b>931</b>
																												-
																												Clarksville,
																												TN</a><br><a
																												href="/934"><b>934</b>
																												-
																												Brentwood,
																												NY</a><br><a
																												href="/936"><b>936</b>
																												-
																												Conroe,
																												TX</a><br><a
																												href="/937"><b>937</b>
																												-
																												Dayton,
																												OH</a><br><a
																												href="/938"><b>938</b>
																												-
																												Huntsville,
																												AL</a><br><a
																												href="/939"><b>939</b>
																												- Puerto
																												Rico</a><br><a
																												href="/940"><b>940</b>
																												-
																												Denton,
																												TX</a><br><a
																												href="/941"><b>941</b>
																												- North
																												Port,
																												FL</a><br><a
																												href="/947"><b>947</b>
																												- Troy,
																												MI</a><br><a
																												href="/949"><b>949</b>
																												-
																												Irvine,
																												CA</a><br><a
																												href="/951"><b>951</b>
																												-
																												Riverside,
																												CA</a><br><a
																												href="/952"><b>952</b>
																												-
																												Bloomington,
																												MN</a><br><a
																												href="/954"><b>954</b>
																												- Fort
																												Lauderdale,
																												FL</a><br><a
																												href="/956"><b>956</b>
																												-
																												Laredo,
																												TX</a><br><a
																												href="/959"><b>959</b>
																												-
																												Hartford,
																												CT</a><br><a
																												href="/970"><b>970</b>
																												- Fort
																												Collins,
																												CO</a><br><a
																												href="/971"><b>971</b>
																												-
																												Portland,
																												OR</a><br><a
																												href="/972"><b>972</b>
																												-
																												Dallas,
																												TX</a><br><a
																												href="/973"><b>973</b>
																												-
																												Newark,
																												NJ</a><br><a
																												href="/978"><b>978</b>
																												-
																												Lowell,
																												MA</a><br><a
																												href="/979"><b>979</b>
																												-
																												College
																												Station,
																												TX</a><br><a
																												href="/980"><b>980</b>
																												-
																												Charlotte,
																												NC</a><br><a
																												href="/984"><b>984</b>
																												-
																												Raleigh,
																												NC</a><br><a
																												href="/985"><b>985</b>
																												- Houma,
																												LA</a><br><a
																												href="/986"><b>986</b>
																												-
																												Idaho</a><br><a
																												href="/989"><b>989</b>
																												-
																												Saginaw,
																												MI</a><br></div>
																		</td>
																	</tr>
																</table>
															</div>
															<div class="col-md-8">
																<h2>By State and Country
													</a></h2>
													<ul class="see-also">
														<li>See also:</li>
														<li><a href="/area-code-list.htm">Detailed List of All Area
																Codes</a></li>
														<li><a href="/area_code_listings_by_state.htm">US Area Codes by
																State</a></li>
														<li><a href="/canadian_area_codes.htm">Canadian Area Codes</a>
														</li>
														<li><a href="/data_request.php">Spreadsheet</a></li>
													</ul>
													<table class="table table-striped">
														<tbody>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/alabama_area_codes.htm">Alabama</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/205">205</a>, <a href="/251">251</a>, <a
																		href="/256">256</a>, <a href="/334">334</a>, <a
																		href="/938">938</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/alaska_area_codes.htm">Alaska</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/907">907</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/arizona_area_codes.htm">Arizona</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/480">480</a>, <a href="/520">520</a>, <a
																		href="/602">602</a>, <a href="/623">623</a>, <a
																		href="/928">928</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/arkansas_area_codes.htm">Arkansas</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/479">479</a>, <a href="/501">501</a>, <a
																		href="/870">870</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/california_area_codes.htm">California</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/209">209</a>, <a href="/213">213</a>, <a
																		href="/279">279</a>, <a href="/310">310</a>, <a
																		href="/323">323</a>, <a href="/408">408</a>, <a
																		href="/415">415</a>, <a href="/424">424</a>, <a
																		href="/442">442</a>, <a href="/510">510</a>, <a
																		href="/530">530</a>, <a href="/559">559</a>, <a
																		href="/562">562</a>, <a href="/619">619</a>, <a
																		href="/626">626</a>, <a href="/628">628</a>, <a
																		href="/650">650</a>, <a href="/657">657</a>, <a
																		href="/661">661</a>, <a href="/669">669</a>, <a
																		href="/707">707</a>, <a href="/714">714</a>, <a
																		href="/747">747</a>, <a href="/760">760</a>, <a
																		href="/805">805</a>, <a href="/818">818</a>, <a
																		href="/820">820</a>, <a href="/831">831</a>, <a
																		href="/858">858</a>, <a href="/909">909</a>, <a
																		href="/916">916</a>, <a href="/925">925</a>, <a
																		href="/949">949</a>, <a href="/951">951</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/canadian_area_codes.htm">Canada</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/204">204</a>, <a href="/226">226</a>, <a
																		href="/236">236</a>, <a href="/249">249</a>, <a
																		href="/250">250</a>, <a href="/289">289</a>, <a
																		href="/306">306</a>, <a href="/343">343</a>, <a
																		href="/365">365</a>, <a href="/367">367</a>, <a
																		href="/403">403</a>, <a href="/416">416</a>, <a
																		href="/418">418</a>, <a href="/431">431</a>, <a
																		href="/437">437</a>, <a href="/438">438</a>, <a
																		href="/450">450</a>, <a href="/506">506</a>, <a
																		href="/514">514</a>, <a href="/519">519</a>, <a
																		href="/548">548</a>, <a href="/579">579</a>, <a
																		href="/581">581</a>, <a href="/587">587</a>, <a
																		href="/604">604</a>, <a href="/613">613</a>, <a
																		href="/639">639</a>, <a href="/647">647</a>, <a
																		href="/705">705</a>, <a href="/709">709</a>, <a
																		href="/778">778</a>, <a href="/780">780</a>, <a
																		href="/782">782</a>, <a href="/807">807</a>, <a
																		href="/819">819</a>, <a href="/825">825</a>, <a
																		href="/867">867</a>, <a href="/873">873</a>, <a
																		href="/902">902</a>, <a href="/905">905</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/colorado_area_codes.htm">Colorado</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/303">303</a>, <a href="/719">719</a>, <a
																		href="/720">720</a>, <a href="/970">970</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/connecticut_area_codes.htm">Connecticut</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/203">203</a>, <a href="/475">475</a>, <a
																		href="/860">860</a>, <a href="/959">959</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/delaware_area_codes.htm">Delaware</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/302">302</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/florida_area_codes.htm">Florida</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/239">239</a>, <a href="/305">305</a>, <a
																		href="/321">321</a>, <a href="/352">352</a>, <a
																		href="/386">386</a>, <a href="/407">407</a>, <a
																		href="/561">561</a>, <a href="/727">727</a>, <a
																		href="/754">754</a>, <a href="/772">772</a>, <a
																		href="/786">786</a>, <a href="/813">813</a>, <a
																		href="/850">850</a>, <a href="/863">863</a>, <a
																		href="/904">904</a>, <a href="/941">941</a>, <a
																		href="/954">954</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/georgia_area_codes.htm">Georgia</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/229">229</a>, <a href="/404">404</a>, <a
																		href="/470">470</a>, <a href="/478">478</a>, <a
																		href="/678">678</a>, <a href="/706">706</a>, <a
																		href="/762">762</a>, <a href="/770">770</a>, <a
																		href="/912">912</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/hawaii_area_codes.htm">Hawaii</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/808">808</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/idaho_area_codes.htm">Idaho</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/208">208</a>, <a href="/986">986</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/illinois_area_codes.htm">Illinois</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/217">217</a>, <a href="/224">224</a>, <a
																		href="/309">309</a>, <a href="/312">312</a>, <a
																		href="/331">331</a>, <a href="/618">618</a>, <a
																		href="/630">630</a>, <a href="/708">708</a>, <a
																		href="/773">773</a>, <a href="/779">779</a>, <a
																		href="/815">815</a>, <a href="/847">847</a>, <a
																		href="/872">872</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/indiana_area_codes.htm">Indiana</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/219">219</a>, <a href="/260">260</a>, <a
																		href="/317">317</a>, <a href="/463">463</a>, <a
																		href="/574">574</a>, <a href="/765">765</a>, <a
																		href="/812">812</a>, <a href="/930">930</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/iowa_area_codes.htm">Iowa</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/319">319</a>, <a href="/515">515</a>, <a
																		href="/563">563</a>, <a href="/641">641</a>, <a
																		href="/712">712</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/kansas_area_codes.htm">Kansas</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/316">316</a>, <a href="/620">620</a>, <a
																		href="/785">785</a>, <a href="/913">913</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/kentucky_area_codes.htm">Kentucky</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/270">270</a>, <a href="/364">364</a>, <a
																		href="/502">502</a>, <a href="/606">606</a>, <a
																		href="/859">859</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/louisiana_area_codes.htm">Louisiana</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/225">225</a>, <a href="/318">318</a>, <a
																		href="/337">337</a>, <a href="/504">504</a>, <a
																		href="/985">985</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/maine_area_codes.htm">Maine</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/207">207</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/maryland_area_codes.htm">Maryland</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/240">240</a>, <a href="/301">301</a>, <a
																		href="/410">410</a>, <a href="/443">443</a>, <a
																		href="/667">667</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/massachusetts_area_codes.htm">Massachusetts</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/339">339</a>, <a href="/351">351</a>, <a
																		href="/413">413</a>, <a href="/508">508</a>, <a
																		href="/617">617</a>, <a href="/774">774</a>, <a
																		href="/781">781</a>, <a href="/857">857</a>, <a
																		href="/978">978</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/michigan_area_codes.htm">Michigan</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/231">231</a>, <a href="/248">248</a>, <a
																		href="/269">269</a>, <a href="/313">313</a>, <a
																		href="/517">517</a>, <a href="/586">586</a>, <a
																		href="/616">616</a>, <a href="/734">734</a>, <a
																		href="/810">810</a>, <a href="/906">906</a>, <a
																		href="/947">947</a>, <a href="/989">989</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/minnesota_area_codes.htm">Minnesota</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/218">218</a>, <a href="/320">320</a>, <a
																		href="/507">507</a>, <a href="/612">612</a>, <a
																		href="/651">651</a>, <a href="/763">763</a>, <a
																		href="/952">952</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/mississippi_area_codes.htm">Mississippi</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/228">228</a>, <a href="/601">601</a>, <a
																		href="/662">662</a>, <a href="/769">769</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/missouri_area_codes.htm">Missouri</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/314">314</a>, <a href="/417">417</a>, <a
																		href="/573">573</a>, <a href="/636">636</a>, <a
																		href="/660">660</a>, <a href="/816">816</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/montana_area_codes.htm">Montana</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/406">406</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/nebraska_area_codes.htm">Nebraska</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/308">308</a>, <a href="/402">402</a>, <a
																		href="/531">531</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/nevada_area_codes.htm">Nevada</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/702">702</a>, <a href="/725">725</a>, <a
																		href="/775">775</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/new_hampshire_area_codes.htm">New
																		Hampshire</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/603">603</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/new_jersey_area_codes.htm">New Jersey</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/201">201</a>, <a href="/551">551</a>, <a
																		href="/609">609</a>, <a href="/640">640</a>, <a
																		href="/732">732</a>, <a href="/848">848</a>, <a
																		href="/856">856</a>, <a href="/862">862</a>, <a
																		href="/908">908</a>, <a href="/973">973</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/new_mexico_area_codes.htm">New Mexico</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/505">505</a>, <a href="/575">575</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/new_york_area_codes.htm">New York</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/212">212</a>, <a href="/315">315</a>, <a
																		href="/332">332</a>, <a href="/347">347</a>, <a
																		href="/516">516</a>, <a href="/518">518</a>, <a
																		href="/585">585</a>, <a href="/607">607</a>, <a
																		href="/631">631</a>, <a href="/646">646</a>, <a
																		href="/680">680</a>, <a href="/716">716</a>, <a
																		href="/718">718</a>, <a href="/838">838</a>, <a
																		href="/845">845</a>, <a href="/914">914</a>, <a
																		href="/917">917</a>, <a href="/929">929</a>, <a
																		href="/934">934</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/north_carolina_area_codes.htm">North
																		Carolina</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/252">252</a>, <a href="/336">336</a>, <a
																		href="/704">704</a>, <a href="/743">743</a>, <a
																		href="/828">828</a>, <a href="/910">910</a>, <a
																		href="/919">919</a>, <a href="/980">980</a>, <a
																		href="/984">984</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/north_dakota_area_codes.htm">North
																		Dakota</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/701">701</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/ohio_area_codes.htm">Ohio</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/216">216</a>, <a href="/220">220</a>, <a
																		href="/234">234</a>, <a href="/330">330</a>, <a
																		href="/380">380</a>, <a href="/419">419</a>, <a
																		href="/440">440</a>, <a href="/513">513</a>, <a
																		href="/567">567</a>, <a href="/614">614</a>, <a
																		href="/740">740</a>, <a href="/937">937</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/oklahoma_area_codes.htm">Oklahoma</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/405">405</a>, <a href="/539">539</a>, <a
																		href="/580">580</a>, <a href="/918">918</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/oregon_area_codes.htm">Oregon</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/458">458</a>, <a href="/503">503</a>, <a
																		href="/541">541</a>, <a href="/971">971</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/pennsylvania_area_codes.htm">Pennsylvania</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/215">215</a>, <a href="/223">223</a>, <a
																		href="/267">267</a>, <a href="/272">272</a>, <a
																		href="/412">412</a>, <a href="/445">445</a>, <a
																		href="/484">484</a>, <a href="/570">570</a>, <a
																		href="/610">610</a>, <a href="/717">717</a>, <a
																		href="/724">724</a>, <a href="/814">814</a>, <a
																		href="/878">878</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/rhode_island_area_codes.htm">Rhode
																		Island</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/401">401</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/south_carolina_area_codes.htm">South
																		Carolina</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/803">803</a>, <a href="/843">843</a>, <a
																		href="/854">854</a>, <a href="/864">864</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/south_dakota_area_codes.htm">South
																		Dakota</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/605">605</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/tennessee_area_codes.htm">Tennessee</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/423">423</a>, <a href="/615">615</a>, <a
																		href="/629">629</a>, <a href="/731">731</a>, <a
																		href="/865">865</a>, <a href="/901">901</a>, <a
																		href="/931">931</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap>
																	Territories</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/340">340</a> (VI), <a href="/670">670</a>
																	(MP), <a href="/671">671</a> (GU), <a
																		href="/684">684</a> (AS), <a href="/787">787</a>
																	(PR), <a href="/939">939</a> (PR)</td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/texas_area_codes.htm">Texas</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/210">210</a>, <a href="/214">214</a>, <a
																		href="/254">254</a>, <a href="/281">281</a>, <a
																		href="/325">325</a>, <a href="/346">346</a>, <a
																		href="/361">361</a>, <a href="/409">409</a>, <a
																		href="/430">430</a>, <a href="/432">432</a>, <a
																		href="/469">469</a>, <a href="/512">512</a>, <a
																		href="/682">682</a>, <a href="/713">713</a>, <a
																		href="/726">726</a>, <a href="/737">737</a>, <a
																		href="/806">806</a>, <a href="/817">817</a>, <a
																		href="/830">830</a>, <a href="/832">832</a>, <a
																		href="/903">903</a>, <a href="/915">915</a>, <a
																		href="/936">936</a>, <a href="/940">940</a>, <a
																		href="/956">956</a>, <a href="/972">972</a>, <a
																		href="/979">979</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/utah_area_codes.htm">Utah</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/385">385</a>, <a href="/435">435</a>, <a
																		href="/801">801</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/vermont_area_codes.htm">Vermont</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/802">802</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/virginia_area_codes.htm">Virginia</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/276">276</a>, <a href="/434">434</a>, <a
																		href="/540">540</a>, <a href="/571">571</a>, <a
																		href="/703">703</a>, <a href="/757">757</a>, <a
																		href="/804">804</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/washington_area_codes.htm">Washington</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/206">206</a>, <a href="/253">253</a>, <a
																		href="/360">360</a>, <a href="/425">425</a>, <a
																		href="/509">509</a>, <a href="/564">564</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/washington_dc_area_codes.htm">Washington,
																		DC</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/202">202</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/west_virginia_area_codes.htm">West
																		Virginia</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/304">304</a>, <a href="/681">681</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/wisconsin_area_codes.htm">Wisconsin</a>
																</td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/262">262</a>, <a href="/414">414</a>, <a
																		href="/534">534</a>, <a href="/608">608</a>, <a
																		href="/715">715</a>, <a href="/920">920</a></td>
															</tr>
															<tr>
																<td style="border-bottom: 1px solid #999999" nowrap><a
																		href="/wyoming_area_codes.htm">Wyoming</a></td>
																<td style="border-bottom: 1px solid #999999"><a
																		href="/307">307</a></td>
															</tr>
														</tbody>
													</table>
												</div>
											</div>

											<div class="ad-unit-parent ">
												<ins class="adsbygoogle ad-unit xs-300x250 sm-468x60 lg-728x90"
													data-ad-client="ca-pub-0709341197255740"
													data-ad-slot="9012842496"></ins>
												<script>
													(adsbygoogle = window.adsbygoogle || []).push({});
												</script>
											</div>

											<br>
											<h2>Where are area codes used?</h2>
											<div class="row">
												<div class="col-md-5" style="text-align: center">
													<a href="/images/npa-coverage.png"><img src="/images/npa-coverage.png" class="img-responsive center-block" style="border: 1px solid #000000; max-height: 300px"></a>
														<a href="/images/npa-coverage.png">(Click to Enlarge)</a>
												</div>
												<div class="col-md-7">
													<p>
														Contrary to what most Americans are likely to believe, area
														codes exist outside of the US.
														There are 405 area codes in the world:
														326 in the US,
														42 in Canada,
														17 non-geographic,
														and 20 others.
														Most of the other area codes are in the Caribbean.
														However, some are located in the Pacific including
														<a href="/684">684</a> (American Samoa), <a href="/671">671</a>
														(Guam), and <a href="/670">670</a> (Northern Mariana Islands).
													</p>
													<p>
														California is the state with the most area codes at 34 followed
														by Texas (27), New York (19), Florida (17), and Illinois (13).
														12 US states only have a single area code. While no area codes
														in the US cross state boundaries, 3 area codes in Canada cross
														province boundaries. </p>
												</div>
											</div>
											<br>
											<h2>Format of a Telephone Number: (NPA) NXX-XXXX</h2>
											<div class="row">
												<div class="col-md-5" style="text-align: center">
													<img src="/images/telephone-number-parts.png" class="img-responsive center-block" alt="telephone number format">
	</div>
													<div class="col-md-7">
														<p>
															In the <a href="/area_code_listings_by_state.htm">US</a> and
															its territories, <a
																href="/canadian_area_codes.htm">Canada</a>, and the
															Caribbean, the organization and allocation of telephone
															numbers is governed by the
															North American Numbering Plan Administration (NANPA). NANPA
															organizes the allocation of area codes and telephone
															prefixes to various phone companies.
															The basic format of a phone number in any of these countries
															is <b>NPA-NXX-XXXX</b> or <b>(NPA) NXX-XXXX</b>.
														</p>
													</div>
												</div>

												<p><b>NPA</b>:
													Area codes came into use during the early 1940s. NPA codes were
													developed by AT&amp;T and the Bell System to divide the coverage
													area into "number plan areas" (abbreviated NPA).
													NPA codes are more commonly referred to as area codes.
													While the system was developed in the 40s, direct dialing of long
													distance did not begin until the early 50s. Some area codes are
													reserved for special purposes. For instance, area code 800 (commonly
													referred to as 800-numbers) is reserved for toll free calls where
													the <i>called</i> party is charged instead
													of the <i>calling</i> party. Also, not all area codes are currently
													in use.
												</p>

												<p><b>NXX</b>:
													The next three digits of a landline number or cellphone number are
													called the NXX. The NXX is also known as the prefix or exchange.
													Various telephone
													carriers will reserve blocks of telephone numbers by reserving an
													NXX within an area code. Like area codes, not all prefixes are
													currently in use.
												</p>

												<p><b>Subscriber</b>:
													Finally, the final 4 digits of the phone number are known as the
													subscriber or local number. Based on the total number of active NPA
													and NXX combinations reserved and that each one
													could have up to 10,000 possible subscriber numbers, the current
													total possible number of telephone numbers is 1,699,140,000. Based
													on the total
													population of the US and Canada according to the US Census and the
													World Bank, that leaves 4 phone numbers for every person.
													Remember though that phone numbers are no longer just used for
													standard home phones. Many telephone numbers are now used for fax
													machines, cell phones or wireless phones, or
													internet connections so one person may actually need multiple phone
													lines.
												</p>

												<div class="ad-unit-parent ">
													<ins class="adsbygoogle ad-unit xs-300x250 sm-468x60 lg-728x90"
														data-ad-client="ca-pub-0709341197255740"
														data-ad-slot="9012842496"></ins>
													<script>
														(adsbygoogle = window.adsbygoogle || []).push({});
													</script>
												</div>

												<br>
												<h2>Assignment of Phone
													Numbers<br><small>The History of Phone Number Allocation</small>
												</h2>
												<br>
												<h3>The 86 Original Area Codes from 1947</h3>
												<div class="row">
													<div class="col-md-5" style="text-align: center">
														<a href="/images/original-1947-area-codes.png"><img src="/images/original-1947-area-codes-thumb.png" class="img-responsive center-block" style="border: 1px solid #000000; max-height: 300px" alt="original 1947 area codes"></a>
															<a href="/images/original-1947-area-codes.png">(Click to
																Enlarge)</a><br>
			</div>
															<div class="col-md-7">
																<p>
																	86 area codes were created by AT&amp;T and the Bell
																	System in 1947.
																	They were created to prepare for a nationwide
																	unified long-distance direct dialing system - the
																	ability to make a call to any other calling area
																	without the need for an operator.
																</p>
																<p>
																	The first digit did not allow a zero (could be
																	confused with the operator) or a 1 (techical
																	reasons).
																	The second digit was either a 0 for an area code
																	covering an entire state/province or 1 for an area
																	code covering part of a state/province.
																</p>
																<p>
																	At the time, rotary phones made it so that dialing
																	lower numbers like 1 or 2 took less time to dial and
																	dialing higher numbers took longer to dial.
																	Area codes with lower numbers that were easier to
																	dial were given to high population and high call
																	volume areas.
																	For this reason, areas such as New York (<a
																		href="/212">area code 212</a> requires 2+1+2=5
																	pulses), Los Angeles (<a href="/213">area code
																		213</a> requires 2+1+3=6 pulses), and Chicago
																	(<a href="/312">area code 312</a> requires 3+1+2=6
																	pulses)
																	received area codes that are much faster to dial
																	than rural areas such as South Dakota (<a
																		href="/605">area code 605</a> requires 6+10+5=21
																	pulses).
																</p>
																<p>
																	The original area codes only existed in the US and
																	Canada. Parts of Canada, Alaska, and Hawaii were not
																	yet included.
																</p>
																<p>
																	The original 86 area codes:<br>
																	<a href="/201">201</a>, <a href="/202">202</a>, <a
																		href="/203">203</a>, <a href="/204">204</a>, <a
																		href="/205">205</a>, <a href="/206">206</a>, <a
																		href="/207">207</a>, <a href="/208">208</a>, <a
																		href="/212">212</a>, <a href="/213">213</a>, <a
																		href="/214">214</a>, <a href="/215">215</a>, <a
																		href="/216">216</a>, <a href="/217">217</a>, <a
																		href="/218">218</a>, <a href="/301">301</a>, <a
																		href="/302">302</a>, <a href="/303">303</a>, <a
																		href="/304">304</a>, <a href="/305">305</a>, <a
																		href="/306">306</a>, <a href="/307">307</a>, <a
																		href="/312">312</a>, <a href="/313">313</a>, <a
																		href="/314">314</a>, <a href="/315">315</a>, <a
																		href="/316">316</a>, <a href="/317">317</a>, <a
																		href="/319">319</a>, <a href="/401">401</a>, <a
																		href="/402">402</a>, <a href="/403">403</a>, <a
																		href="/404">404</a>, <a href="/405">405</a>, <a
																		href="/406">406</a>, <a href="/412">412</a>, <a
																		href="/413">413</a>, <a href="/414">414</a>, <a
																		href="/415">415</a>, <a href="/416">416</a>, <a
																		href="/418">418</a>, <a href="/419">419</a>, <a
																		href="/501">501</a>, <a href="/502">502</a>, <a
																		href="/503">503</a>, <a href="/504">504</a>, <a
																		href="/505">505</a>, <a href="/512">512</a>, <a
																		href="/513">513</a>, <a href="/514">514</a>, <a
																		href="/515">515</a>, <a href="/517">517</a>, <a
																		href="/518">518</a>, <a href="/601">601</a>, <a
																		href="/602">602</a>, <a href="/603">603</a>, <a
																		href="/604">604</a>, <a href="/605">605</a>, <a
																		href="/612">612</a>, <a href="/613">613</a>, <a
																		href="/614">614</a>, <a href="/616">616</a>, <a
																		href="/617">617</a>, <a href="/618">618</a>, <a
																		href="/701">701</a>, <a href="/702">702</a>, <a
																		href="/703">703</a>, <a href="/704">704</a>, <a
																		href="/712">712</a>, <a href="/713">713</a>, <a
																		href="/715">715</a>, <a href="/716">716</a>, <a
																		href="/717">717</a>, <a href="/801">801</a>, <a
																		href="/802">802</a>, <a href="/803">803</a>, <a
																		href="/812">812</a>, <a href="/814">814</a>, <a
																		href="/815">815</a>, <a href="/816">816</a>, <a
																		href="/901">901</a>, <a href="/902">902</a>, <a
																		href="/913">913</a>, <a href="/914">914</a>, <a
																		href="/915">915</a>, and <a href="/916">916</a>
																</p>
															</div>
													</div>
													<br>

													<h3>The Growing Need for New Area Codes</h3>
													<div class="row">
														<div class="col-md-5" style="text-align: center">
															<b>General Purpose Area Codes Introduced by Decade</b>
															<div class="D3ChartOuterContainer">
																<div class="D3ChartContainer">
																	<div class="D3SizingContainer"><svg id="BarChart0"
																			class="BarChart"></svg></div>
																</div>
															</div>
														</div>
														<div class="col-md-7">
															<p>
																When the phone formats we commonly use today first came
																into service in the 1940s and the 1950s, blocks of phone
																numbers were allocated to a phone carrier in 10,000
																phone numbers (ie. an entire 6 digit prefix).
																Frequently, the 10,000 numbers would be enough for a
																small town with larger towns being allocated multiple
																prefixes.
																Further, local phone carriers frequently had a monopoly
																on local phone service which prevented large portions of
																an allocated block from being unutilized.
															</p>
															<p>
																In the 1990s, cell phones became much more popular which
																created an explosion of demand for new phone numbers.
																Cell phones also reduced the monopoly of local phone
																providers which reduced utilization of allocated
																prefixes.
																Instead of a single primary phone carrier, cities had
																two or more carriers - each needing their own prefix.
																In addition, the rise in popularity in the internet
																(dial up and DSL) and voice over IP (VOIP), local
																interenet service providers and cable companies started
																to request prefixes.
																Many of these prefixes included few, if any,
																subscribers.
															</p>
														</div>
													</div>
													<br>
													<h3>The Decline of Splits in Favor of Overlays</h3>
													<div class="row">
														<div class="col-md-5" style="text-align: center">
															<b>Splits and Overlays by Year</b>
															<div class="D3ChartOuterContainer">
																<div class="D3ChartContainer">
																	<div class="D3SizingContainer"><svg id="LineChart0"
																			class="LineChart"></svg></div>
																</div>
															</div>
														</div>
														<div class="col-md-7">
															<p>
																For decades, new area codes were created through a
																"split" of an existing area code into multiple regions.
																Normally, the more populated region would continue to
																use the existing area code.
																The less populated areas would have all existing phone
																numbers reassigned to use a new area code to free up
																more numbers in the original area code.
																This process forced many into a new phone number which
																would require updates to letterhead, business cards,
																phone directories, personal contact lists, etc.
																Many people would dial the incorrect area code which
																caused confusion.
															</p>
															<p>
																In 1992, <a href="/917">area code 917</a> was created as
																the first "overlay" area code.
																With an overlay area code, the overlay serves the same
																geographic as the original to increase the pool of
																numbers available in the area.
																When the original phone systems were put in place,
																7-digit dialing (without the area code) could be used to
																make local calls, and 10-digit dialing (with the area
																code) only needed to be used for long distance calls.
																<!--Initial overlay area codes did not require 10 digit dialing.
			Instead phone numbers were allocated in such a way that local calls could be correctly routed to the correct area code for the phone number, but this process prevented full utilization of the area codes.-->
																In 1997, <a href="/301">area code 301</a> was introduced
																as the first overlay with forced 10 digit dialing for
																local calls.
																Initially, there was substantial public resistance to
																overlays because of the 10-digit dialing requirement for
																local calls.
																However, the last area code split in Canada was in 1999
																with the split of <a href="/403">403</a> splitting off
																<a href="/780">780</a> and the last area code split in
																the US was in 2007 with <a href="/505">505</a> splitting
																off <a href="/575">575</a>.
																No area code splits are currently proposed and both
																countries have agreed: without exceptional
																circumstances, all new area codes will be overlays.
															</p>
															<p>
																Today, 7-digit dialing is broken in most major cities.
																The few major cities where 10-digit dialing is not
																required include Detroit, El Paso, Jacksonville,
																Louisville, Memphis, Milwaukee and Oklahoma City.
																Many areas not served by an overlay can still use
																7-digit dialing.
															</p>
														</div>
													</div>
													<br>
													<h3>The Effect of Number Pooling</h3>
													<div class="row">
														<div class="col-md-5" style="text-align: center">
															<b>Prefixes Introduced by Year in the US</b>
															<div class="D3ChartOuterContainer">
																<div class="D3ChartContainer">
																	<div class="D3SizingContainer"><svg id="BarChart1"
																			class="BarChart"></svg></div>
																</div>
															</div>
															<center>
																<div
																	style="display: inline-block; width: 15px; height: 15px; background-color: #1f77B4; vertical-align: text-top">
																</div> Before Number Pooling &nbsp;
																<div
																	style="display: inline-block; width: 15px; height: 15px; background-color: #aec7e8; vertical-align: text-top">
																</div> After Number Pooling
															</center>
														</div>
														<div class="col-md-7">
															<p>
																In 1998, the North American Numbering Plan
																Administration (NANPA) estimated that all area codes for
																a 10-digit dialing system would run out by 2025.
																Something besides allocating more area codes needed to
																be done to improve the system.
																After a few trials, mandatory number pooling was
																implemented in 2002 with a national rollout to the 100
																largest metropolitan areas.
																With number pooling, an entire prefix of 10,000 numbers
																is allocated to a specific area, but phone numbers are
																only allocated to a specific carrier in 1,000 block
																increments.
																Further, in US markets where number pooling is required,
																service providers are required to return blocks of 1,000
																numbers that are more than 90% unutilized.
															</p>
															<p>
																While several US markets are still not required to
																implement number pooling and Canada has no number
																pooling, the effects dramatically slowed the need to
																allocate new prefixes and new area codes because of
																increased utilization.
																The rate of issuing new area codes dropped to nearly
																half that of the 1990s.
															</p>
														</div>
													</div>
													<br>
													<h2>Modern Usage</h2>
													<div class="row">
														<div class="col-xs-6 col-xs-offset-3 col-md-3 col-md-offset-1"
															style="text-align: center">
															<b>Primary Prefix Usage</b>
															<div class="D3ChartOuterContainer">
																<div class="D3ChartContainer"
																	style='padding-bottom: 100%'>
																	<div class="D3SizingContainer"><svg id="PieChart0"
																			class="PieChart"></svg></div>
																</div>
															</div>
														</div>
														<div class="col-md-7 col-md-offset-1">
															<p>
																While it may seem that all consumers in the US use a
																mobile phone, more than two-thirds of prefixes are
																allocated for landline use.
																A 2017 study by the National Center for Health
																Statistics, 43% of US households still use a landline
																phone.
																That number has been dropping by about 3.5% per year
																since 2010 (would would make the 2022 estimate 26%).
																Many businesses, home internet services, and
																voice-over-IP (VOIP) phones also account for increased
																landline usage.
															</p>
														</div>
													</div>
													<br>
													<h2>Non-Geographic Area Codes</h2>
													<p>
														Not all area codes are assigned to a specific geographic area.
														One of the most common are toll-free area codes where the caller
														is not billed for long distance (though wireless customers may
														have minutes deducted from their plan):
														800, 833, 844, 855, 866, 877, and 888. </p>
													<p>
														The 900 area code is also currently used for premium services
														that are billed to the caller at higher than normal long
														distance rates.
														In the 1980s and and early 1990s, 900 numbers were frequently
														used to target children to run up phone bills, psychic hotlines,
														adult entertainment, computer help, etc.
														Legislative protections in the 1990s and the withdrawal of phone
														companies from passing these fees onto customers has largely
														killed the 900-number industry.
													</p>
													<p>
														Other caller-pays area codes include
														500, 521, 522, 533, 544, 566, 577, 588, and 622. Though they see
														much less usage now, some are still used for dial-up modem
														access or security systems.
													</p>
													<p>
														Area codes 600 and 700 are reserved for special
														telecommunications services and receive little usage.
													</p>
													<br>
													<h2>Area Code Tools</h2>

													<p>For looking up information on a specific phone number, the <a
															href="/reverse-phone-lookup/">free reverse phone lookup</a>
														allows you to see the name and address of
														phone numbers listed in the white pages of phone books
														throughout the US. For unlisted or cell phone
														numbers, we provide a convenient price comparison of popular
														services that allow you to search deeper for
														the owner of a phone number.</p>

													<p>To find information on a specific area code, use the <a
															href="/area-code-lookup/">area code lookup</a> that
														makes it easy to find an area code by number and gives detailed
														information including city/state, timezone, and
														<a href="/area-code-map.htm">area code maps</a>. If you are
														looking for the area code for a particular city,
														you can <a href="/area-code-locator/">search area codes by
															city</a> using our area code finder.</p>

													<p> To browse all area codes, we have a
														list of all United States <a
															href="/area_code_listings_by_state.htm">area codes by
															state</a> and
														<a href="/area-code-list.htm">area codes by number</a>. The <a
															href="/area-code-list.htm">area code list</a> includes
														a printable copy that you can print and use for reference.</p>

													<p>For international numbers, we also include <a
															href="/canadian_area_codes.htm">Canadian area codes</a>.
														For dialing internationally, see the list of <a
															href="/international_dialing_codes.htm">international
															dialing codes</a> with
														instructions on how to dial foreign numbers or dial
														U.S./Canadian number while traveling internationally.</p>


													<div class="ad-unit-parent ">
														<ins class="adsbygoogle ad-unit xs-300x250 sm-468x60 lg-728x90"
															data-ad-client="ca-pub-0709341197255740"
															data-ad-slot="9012842496"></ins>
														<script>
															(adsbygoogle = window.adsbygoogle || []).push({});
														</script>
													</div>

												</div>
											</div>


											<div class="row footer">
												<div class="col-xs-12">
													<div class="row">
														<div class="col-xs-12"
															style="border-bottom: 1px solid #eee; padding: 0; margin-top: 1em;">
														</div>
														<div class="col-xs-12" id="footer-links">
															<div class="col-md-9">
																<h3>Listings by US State</h3>
																<ul class="states">
																	<li><a href='/alabama_area_codes.htm'>Alabama</a>
																	</li>
																	<li><a href='/alaska_area_codes.htm'>Alaska</a></li>
																	<li><a href='/arizona_area_codes.htm'>Arizona</a>
																	</li>
																	<li><a href='/arkansas_area_codes.htm'>Arkansas</a>
																	</li>
																	<li><a
																			href='/california_area_codes.htm'>California</a>
																	</li>
																	<li><a href='/colorado_area_codes.htm'>Colorado</a>
																	</li>
																	<li><a
																			href='/connecticut_area_codes.htm'>Connecticut</a>
																	</li>
																	<li><a href='/delaware_area_codes.htm'>Delaware</a>
																	</li>
																	<li><a href='/florida_area_codes.htm'>Florida</a>
																	</li>
																	<li><a href='/georgia_area_codes.htm'>Georgia</a>
																	</li>
																	<li><a href='/hawaii_area_codes.htm'>Hawaii</a></li>
																	<li><a href='/idaho_area_codes.htm'>Idaho</a></li>
																	<li><a href='/illinois_area_codes.htm'>Illinois</a>
																	</li>
																	<li><a href='/indiana_area_codes.htm'>Indiana</a>
																	</li>
																	<li><a href='/iowa_area_codes.htm'>Iowa</a></li>
																	<li><a href='/kansas_area_codes.htm'>Kansas</a></li>
																	<li><a href='/kentucky_area_codes.htm'>Kentucky</a>
																	</li>
																	<li><a
																			href='/louisiana_area_codes.htm'>Louisiana</a>
																	</li>
																	<li><a href='/maine_area_codes.htm'>Maine</a></li>
																	<li><a href='/maryland_area_codes.htm'>Maryland</a>
																	</li>
																	<li><a
																			href='/massachusetts_area_codes.htm'>Massachusetts</a>
																	</li>
																	<li><a href='/michigan_area_codes.htm'>Michigan</a>
																	</li>
																	<li><a
																			href='/minnesota_area_codes.htm'>Minnesota</a>
																	</li>
																	<li><a
																			href='/mississippi_area_codes.htm'>Mississippi</a>
																	</li>
																	<li><a href='/missouri_area_codes.htm'>Missouri</a>
																	</li>
																	<li><a href='/montana_area_codes.htm'>Montana</a>
																	</li>
																	<li><a href='/nebraska_area_codes.htm'>Nebraska</a>
																	</li>
																	<li><a href='/nevada_area_codes.htm'>Nevada</a></li>
																	<li><a href='/new_hampshire_area_codes.htm'>New
																			Hampshire</a></li>
																	<li><a href='/new_jersey_area_codes.htm'>New
																			Jersey</a></li>
																	<li><a href='/new_mexico_area_codes.htm'>New
																			Mexico</a></li>
																	<li><a href='/new_york_area_codes.htm'>New York</a>
																	</li>
																	<li><a href='/north_carolina_area_codes.htm'>North
																			Carolina</a></li>
																	<li><a href='/north_dakota_area_codes.htm'>North
																			Dakota</a></li>
																	<li><a href='/ohio_area_codes.htm'>Ohio</a></li>
																	<li><a href='/oklahoma_area_codes.htm'>Oklahoma</a>
																	</li>
																	<li><a href='/oregon_area_codes.htm'>Oregon</a></li>
																	<li><a
																			href='/pennsylvania_area_codes.htm'>Pennsylvania</a>
																	</li>
																	<li><a href='/rhode_island_area_codes.htm'>Rhode
																			Island</a></li>
																	<li><a href='/south_carolina_area_codes.htm'>South
																			Carolina</a></li>
																	<li><a href='/south_dakota_area_codes.htm'>South
																			Dakota</a></li>
																	<li><a
																			href='/tennessee_area_codes.htm'>Tennessee</a>
																	</li>
																	<li><a href='/texas_area_codes.htm'>Texas</a></li>
																	<li><a href='/utah_area_codes.htm'>Utah</a></li>
																	<li><a href='/vermont_area_codes.htm'>Vermont</a>
																	</li>
																	<li><a href='/virginia_area_codes.htm'>Virginia</a>
																	</li>
																	<li><a
																			href='/washington_area_codes.htm'>Washington</a>
																	</li>
																	<li><a href='/washington_dc_area_codes.htm'>Washington,
																			DC</a></li>
																	<li><a href='/west_virginia_area_codes.htm'>West
																			Virginia</a></li>
																	<li><a
																			href='/wisconsin_area_codes.htm'>Wisconsin</a>
																	</li>
																	<li><a href='/wyoming_area_codes.htm'>Wyoming</a>
																	</li>
																</ul>
															</div>

															<div class="col-md-3">
																<h3>More Information</h3>
																<ul>
																	<li><a href="/what-is-my-area-code.php">My Area
																			Code</a></li>
																	<li><a href="/data_request.php">Downloadable
																			Database</a></li>
																	<li><a href="/international_dialing_codes.htm">International
																			Dialing Codes</a></li>
																	<li><a href="/canadian_area_codes.htm">Canadian Area
																			Codes</a></li>
																	<li><a href='/american_samoa_area_codes.htm'>American
																			Samoa</a></li>
																	<li><a href='/guam_area_codes.htm'>Guam</a></li>
																	<li><a
																			href='/northern_mariana_islands_area_codes.htm'>Northern
																			Mariana Islands</a></li>
																	<li><a href='/puerto_rico_area_codes.htm'>Puerto
																			Rico</a></li>
																	<li><a href='/virgin_islands_area_codes.htm'>Virgin
																			Islands</a></li>
																	<li><a href="/articles.php">Articles &amp;
																			Infographics</a></li>
																	<li><a href="/area_code_listings_by_state.htm">Area
																			Codes by State</a></li>
																</ul>
															</div>
														</div>
													</div>
												</div>


												<div class="col-xs-12">
													<div class="row" id="footer-bottom">

														<div class="col-xs-12 col-sm-4">
															<a href="/"><img src="/images/logo_small_transparent.cache_extend.1660602886.png" alt="All Area Codes"></a>
														</div>

														<div class="col-xs-12 col-sm-8" id="footer-nav">

															<ul>
																<li><a href="/about_us.htm">About Us</a></li>
																<li><a href="/remove_name.htm">Remove Name</a></li>
																<li><a href="/contact_us.htm">Contact Us</a></li>
																<li><a href="/policies.htm">Privacy &amp; Terms</a></li>
															</ul>

															<small>Copyright 2002-2022</small>
														</div>
													</div>
												</div>
											</div>

										</div>
										<script
											src="/automin/16fa6da1109a534262b1a7c00b90b29cd2f95187.automin.cache_extend.1638201401.js">
										</script>

										<!-- Matomo -->
										<script type="text/javascript">
											var _paq = window._paq || [];



		_paq.push(['trackPageView']);
		_paq.push(['enableLinkTracking']);


var piwik_attribution_url;
_paq.push([function() {
	piwik_attribution_url = this.getAttributionReferrerUrl();
}]);

		(function() {
			var u="//www.aatrk.com/stats/";
			_paq.push(['setTrackerUrl', u+'matomo.php']);
			_paq.push(['setSiteId', '16']);
			var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
			g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
		})();
										</script>
										<noscript>
											<p><img src="//www.aatrk.com/stats/matomo.php?idsite=16&amp;rec=1" style="border:0;" alt="" /></p>
										</noscript>
										<!-- End Matomo Code -->
										<script>
											$().ready(function() {
		$('.codes_container').hide();
					$('#codes_2').show();
			});
										</script>
										<script src="/shared-assets/d3-3.5.9.min.cache_extend.1638201401.js"
											charset="utf-8"></script>
										<script src="/shared-assets/nv.d3-1.8.1.min.cache_extend.1638201401.js">
										</script>
										<script>
											var BarChart0_data;
			var BarChart0_chart;
			var BarChart0_svg;
			nv.addGraph(function() {
				var data = [{"key":"Data","values":[{"x":"1940s","y":87},{"x":"1950s","y":30},{"x":"1960s","y":4},{"x":"1970s","y":1},{"x":"1980s","y":9},{"x":"1990s","y":133},{"x":"2000s","y":72},{"x":"2010s","y":51}]}];

				var chart = nv.models.discreteBarChart();

				var svg = d3.select('#BarChart0');


				chart.margin({ top: 30, right: 20, bottom: 20, left: 50 })
				if (typeof chart.legend != 'undefined') chart.legend.margin().right -= 30;

						if (typeof chart.yScale != 'undefined') {
							chart.margin().left -= 3*8;
						}

				if (typeof chart.legend != 'undefined') {
					chart.legend.vers('furious');
				}
				chart.color(["#1f77b4"]);
			var y_window_formats = 0;
			nv.utils.windowResize(function() {
				y_window_formats = 0;
			});
			if (typeof chart.dispatch.stateChange != 'undefined') {
				// some charts (including bar charts) don't have state changes
				chart.dispatch.on('stateChange.y_window_formats', function () {
					y_window_formats = 0;
				});
			}
			if (typeof chart.yAxis != 'undefined') {	
				// some charts (including pie charts) don't have a y axis
				chart.yAxis.tickFormat(function (d) {
					if (chart.yScale().domain()[1] < 10) {
						return d3.format(',')(d);
					} else {
						// tooltip via https://github.com/novus/nvd3/issues/428
						if (this === window) {
							if (y_window_formats >= 2) {
								return d3.format(',')(d);
							}
							y_window_formats++;
						}

						// axis
						return d3.format(',.0f')(d);
					}
				});
			}
			if (typeof chart.valueFormat == 'function') {
				// over bar
				chart.valueFormat(function (d) {
						return d3.format(',')(d);
					});
			}

					chart.color(["#1f77b4"]);

					if (parseInt(svg.style('width')) < 768/2) {
						chart.staggerLabels(true);
						chart.margin().bottom += 15;
					}


				svg.datum(data)
					.call(chart);

				nv.utils.windowResize(function() { chart.update() });

				BarChart0_data = data;
				BarChart0_chart = chart;
				BarChart0_svg = svg;

				return chart;
			}, function() { 

			});
										</script>
										<script>
											var LineChart0_data;
			var LineChart0_chart;
			var LineChart0_svg;
			var LineChart0_x_annotations;
			var LineChart0_y_annotations;
			nv.addGraph(function() {
				var data = [{"key":"Overlay","values":[{"x":1995,"y":5},{"x":1996,"y":8},{"x":1997,"y":11},{"x":1998,"y":7},{"x":1999,"y":9},{"x":2000,"y":4},{"x":2001,"y":14},{"x":2002,"y":3},{"x":2003,"y":1},{"x":2004,"y":null},{"x":2005,"y":2},{"x":2006,"y":4},{"x":2007,"y":2},{"x":2008,"y":3},{"x":2009,"y":7},{"x":2010,"y":6}]},{"key":"Split","values":[{"x":1995,"y":9},{"x":1996,"y":12},{"x":1997,"y":30},{"x":1998,"y":13},{"x":1999,"y":14},{"x":2000,"y":9},{"x":2001,"y":12},{"x":2002,"y":6},{"x":2003,"y":2},{"x":2004,"y":1},{"x":2005,"y":null},{"x":2006,"y":null},{"x":2007,"y":1},{"x":2008,"y":null},{"x":2009,"y":null},{"x":2010,"y":null}]}];

				var chart = nv.models.lineChart()
					.useInteractiveGuideline(true);

				var svg = d3.select('#LineChart0');

				var x_annotations = [];
				var y_annotations = [];


				chart.margin({ top: 30, right: 20, bottom: 20, left: 50 })
				if (typeof chart.legend != 'undefined') chart.legend.margin().right -= 30;

						if (typeof chart.yScale != 'undefined') {
							chart.margin().left -= 3*8;
						}

				if (typeof chart.legend != 'undefined') {
					chart.legend.vers('furious');
				}

			var y_window_formats = 0;
			nv.utils.windowResize(function() {
				y_window_formats = 0;
			});
			if (typeof chart.dispatch.stateChange != 'undefined') {
				// some charts (including bar charts) don't have state changes
				chart.dispatch.on('stateChange.y_window_formats', function () {
					y_window_formats = 0;
				});
			}
			if (typeof chart.yAxis != 'undefined') {	
				// some charts (including pie charts) don't have a y axis
				chart.yAxis.tickFormat(function (d) {
					if (chart.yScale().domain()[1] < 10) {
						return d3.format(',')(d);
					} else {
						// tooltip via https://github.com/novus/nvd3/issues/428
						if (this === window) {
							if (y_window_formats >= 2) {
								return d3.format(',')(d);
							}
							y_window_formats++;
						}

						// axis
						return d3.format(',.0f')(d);
					}
				});
			}
			if (typeof chart.valueFormat == 'function') {
				// over bar
				chart.valueFormat(function (d) {
						return d3.format(',')(d);
					});
			}
		chart.forceY(0);

					if (data.length > 2 && parseInt(svg.style('width')) < 768/2) {
						chart.showLegend(false);
					}


				svg.datum(data)
					.call(chart);

				nv.utils.windowResize(function() { chart.update(); });

				chart.dispatch.on('renderEnd.alignAnnotations', function () {


				});

				LineChart0_data = data;
				LineChart0_chart = chart;
				LineChart0_svg = svg;
				LineChart0_x_annotations = x_annotations;
				LineChart0_y_annotations = y_annotations;

				return chart;
			}, function() { 

			});
										</script>
										<script>
											var BarChart1_data;
			var BarChart1_chart;
			var BarChart1_svg;
			nv.addGraph(function() {
				var data = [{"key":"Data","values":[{"x":"1998","y":14594},{"x":"1999","y":14063},{"x":"2000","y":13227},{"x":"2001","y":14275},{"x":"2002","y":7790},{"x":"2003","y":3564},{"x":"2004","y":2762},{"x":"2005","y":2725}]}];

				var chart = nv.models.discreteBarChart();

				var svg = d3.select('#BarChart1');


				chart.margin({ top: 30, right: 20, bottom: 20, left: 50 })
				if (typeof chart.legend != 'undefined') chart.legend.margin().right -= 30;

				if (typeof chart.legend != 'undefined') {
					chart.legend.vers('furious');
				}
				chart.color(["#1f77b4","#1f77b4","#1f77b4","#1f77b4","#aec7e8","#aec7e8","#aec7e8","#aec7e8"]);
			var y_window_formats = 0;
			nv.utils.windowResize(function() {
				y_window_formats = 0;
			});
			if (typeof chart.dispatch.stateChange != 'undefined') {
				// some charts (including bar charts) don't have state changes
				chart.dispatch.on('stateChange.y_window_formats', function () {
					y_window_formats = 0;
				});
			}
			if (typeof chart.yAxis != 'undefined') {	
				// some charts (including pie charts) don't have a y axis
				chart.yAxis.tickFormat(function (d) {
					if (chart.yScale().domain()[1] < 10) {
						return d3.format(',')(d);
					} else {
						// tooltip via https://github.com/novus/nvd3/issues/428
						if (this === window) {
							if (y_window_formats >= 2) {
								return d3.format(',')(d);
							}
							y_window_formats++;
						}

						// axis
						return d3.format(',.0f')(d);
					}
				});
			}
			if (typeof chart.valueFormat == 'function') {
				// over bar
				chart.valueFormat(function (d) {
						return d3.format(',')(d);
					});
			}

					chart.color(["#1f77b4","#1f77b4","#1f77b4","#1f77b4","#aec7e8","#aec7e8","#aec7e8","#aec7e8"]);

					if (parseInt(svg.style('width')) < 768/2) {
						chart.staggerLabels(true);
						chart.margin().bottom += 15;
					}


				svg.datum(data)
					.call(chart);

				nv.utils.windowResize(function() { chart.update() });

				BarChart1_data = data;
				BarChart1_chart = chart;
				BarChart1_svg = svg;

				return chart;
			}, function() { 

			});
										</script>
										<script>
											var PieChart0_data;
			var PieChart0_chart;
			var PieChart0_svg;
			nv.addGraph(function() {
				var data = [{"key":"Data","values":[{"x":"Landline","y":117725},{"x":"Unknown","y":1001},{"x":"Wireless","y":51188}]}];

				var total = 0;
				data[0].values.forEach(function (d) {
					total = total + d.y;
				});

				var chart = nv.models.pieChart();

				var svg = d3.select('#PieChart0');


				chart.margin({ top: 30, right: 20, bottom: 20, left: 50 })
				if (typeof chart.legend != 'undefined') chart.legend.margin().right -= 30;
				chart.showLegend(false);

			var y_window_formats = 0;
			nv.utils.windowResize(function() {
				y_window_formats = 0;
			});
			if (typeof chart.dispatch.stateChange != 'undefined') {
				// some charts (including bar charts) don't have state changes
				chart.dispatch.on('stateChange.y_window_formats', function () {
					y_window_formats = 0;
				});
			}
			if (typeof chart.yAxis != 'undefined') {	
				// some charts (including pie charts) don't have a y axis
				chart.yAxis.tickFormat(function (d) {
					if (chart.yScale().domain()[1] < 10) {
						return d3.format(',')(d);
					} else {
						// tooltip via https://github.com/novus/nvd3/issues/428
						if (this === window) {
							if (y_window_formats >= 2) {
								return d3.format(',')(d);
							}
							y_window_formats++;
						}

						// axis
						return d3.format(',.0f')(d);
					}
				});
			}
			if (typeof chart.valueFormat == 'function') {
				// over bar
				chart.valueFormat(function (d) {
						return d3.format(',')(d);
					});
			}
		chart.margin({top: 5, right: 5, bottom: 5, left: 5});

					chart.tooltip.valueFormatter(function (d) {
						return (d/total*100).toFixed() + ' %';
					});



				chart.growOnHover(false);

				if (!chart.labelsOutside()) {

					// the current nvd3 version makes the following adjustment even if growOnHover is turned off
					// need to undo it
					// the result is a pie chart that doesn't fill the entire container
					//d.outer = (d.outer - d.outer / 5)

					var arcs = chart.arcsRadius();
					var new_arcs = [];
					if (arcs.length === 0) {
						data[0].values.forEach(function (d) {
							new_arcs.push({ outer: 1.25, inner: 0 });
						});
					} else {
						arcs.forEach(function (d) {
							new_arcs.push({ outer: d.outer*1.25, inner: d.inner*1.25 });
						});
					}
					chart.arcsRadius(new_arcs);
				}


				// note that a pie chart uses a different data format
				svg.datum(data[0].values)
					.call(chart);

				nv.utils.windowResize(function() { chart.update(); });

				PieChart0_data = data;
				PieChart0_chart = chart;
				PieChart0_svg = svg;

				return chart;
			}, function() { 

			});
										</script>
</body>

</html>'''

soup = BeautifulSoup(response, "html.parser")
codes = soup.find("div", {"id": "codes_2"}).parent.findAll("a")
phone_codes = {}
for code in codes:
    string = code.getText().replace("\n", "")
    code = string[:string.index("-")].replace("\t", "")
    name = re.sub(r"\t+", " ", string=string[string.index("-") + 1:]).strip().replace(", ", ",").replace(",", " ")
    phone_codes[code] = name
print(phone_codes)
