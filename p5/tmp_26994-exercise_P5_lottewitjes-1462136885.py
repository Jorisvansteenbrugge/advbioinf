<!DOCTYPE html>
<html class="" lang="en">
<head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<meta content="IE=edge" http-equiv="X-UA-Compatible">
<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py · master · Witjes, Lotte / advanced_bioinformatics" property="og:title">
<meta content="GitLab Community Edition" property="og:description">
<meta content="https://git.wur.nl/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="og:image">
<meta content="https://git.wur.nl/witje010/advanced_bioinformatics/blob/master/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py · master · Witjes, Lotte / advanced_bioinformatics" property="twitter:title">
<meta content="GitLab Community Edition" property="twitter:description">
<meta content="https://git.wur.nl/assets/gitlab_logo-7ae504fe4f68fdebb3c2034e36621930cd36ea87924c11ff65dbcb8ed50dca58.png" property="twitter:image">

<title>exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py · master · Witjes, Lotte / advanced_bioinformatics · GitLab</title>
<meta content="GitLab Community Edition" name="description">
<link rel="shortcut icon" type="image/x-icon" href="/assets/favicon-075eba76312e8421991a0c1f89a89ee81678bcde72319dd3e8047e2a47cd3a42.ico" />
<link rel="stylesheet" media="all" href="/assets/application-38908eed79ad15cd6109e9ea2e538ea59413fe31ea5bef76f3136479849730e4.css" />
<link rel="stylesheet" media="print" href="/assets/print-68eed6d8135d858318821e790e25da27b2b4b9b8dbb1993fa6765d8e2e3e16ee.css" />
<script src="/assets/application-5df86a0341501ab9771ef0d74471360f66490fada4b1c60aefac19f3e6e2e775.js"></script>
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="WOfVslEbCde/l6HvUIdBQsXJWlMzwhqPYQy/40mvqxgdmEcCr7vo4WySTZj7omOF+7Br0CQHgdsta5/c1WH1ZQ==" />
<meta content="origin-when-cross-origin" name="referrer">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#474D57" name="theme-color">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-5a9cee0e8a51212e70b90c87c12f382c428870c0ff67d1eb034d884b78d2dae7.png" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-a6eec6aeb9da138e507593b464fdac213047e49d3093fc30e90d9a995df83ba3.png" sizes="76x76" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-iphone-retina-72e2aadf86513a56e050e7f0f2355deaa19cc17ed97bbe5147847f2748e5a3e3.png" sizes="120x120" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/touch-icon-ipad-retina-8ebe416f5313483d9c1bc772b5bbe03ecad52a54eba443e5215a22caed2a16a2.png" sizes="152x152" />
<link color="rgb(226, 67, 41)" href="/assets/logo-d36b5212042cebc89b96df4bf6ac24e43db316143e89926c0db839ff694d2de4.svg" rel="mask-icon">
<meta content="/assets/msapplication-tile-1196ec67452f618d39cdd85e2e3a542f76574c071051ae7effbfde01710eb17d.png" name="msapplication-TileImage">
<meta content="#30353E" name="msapplication-TileColor">




<style>
  [data-user-is] {
    display: none !important;
  }
  
  [data-user-is=""] {
    display: block !important;
  }
  
  [data-user-is=""][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not] {
    display: block !important;
  }
  
  [data-user-is-not][data-display="inline"] {
    display: inline !important;
  }
  
  [data-user-is-not=""] {
    display: none !important;
  }
</style>

</head>

<body class="ui_green" data-group="" data-page="projects:blob:show" data-project="advanced_bioinformatics">
<script>
//<![CDATA[
window.gon={};gon.api_version="v3";gon.default_avatar_url="https:\/\/git.wur.nl\/assets\/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.relative_url_root="";gon.shortcuts_path="\/help\/shortcuts";gon.user_color_scheme="white";gon.award_menu_url="\/emojis";
//]]>
</script>

<header class="navbar navbar-fixed-top navbar-gitlab with-horizontal-nav">
<div class="container-fluid">
<div class="header-content">
<button aria-label="Toggle global navigation" class="side-nav-toggle" type="button">
<span class="sr-only">Toggle navigation</span>
<i class="fa fa-bars"></i>
</button>
<button class="navbar-toggle" type="button">
<span class="sr-only">Toggle navigation</span>
<i class="fa fa-ellipsis-v"></i>
</button>
<div class="navbar-collapse collapse">
<ul class="nav navbar-nav">
<li class="hidden-sm hidden-xs">
<div class="has-location-badge search search-form">
<form class="navbar-form" action="/search" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><div class="search-input-container">
<div class="location-badge">This project</div>
<div class="search-input-wrap">
<div class="dropdown" data-url="/search/autocomplete">
<input type="search" name="search" id="search" placeholder="Search" class="search-input dropdown-menu-toggle" spellcheck="false" tabindex="1" autocomplete="off" data-toggle="dropdown" />
<div class="dropdown-menu dropdown-select">
<div class="dropdown-content"><ul>
<li>
<a class="is-focused dropdown-menu-empty-link">
Loading...
</a>
</li>
</ul>
</div><div class="dropdown-loading"><i class="fa fa-spinner fa-spin"></i></div>
</div>
<i class="search-icon"></i>
<i class="clear-icon js-clear-input"></i>
</div>
</div>
</div>
<input type="hidden" name="group_id" id="group_id" />
<input type="hidden" name="project_id" id="search_project_id" value="1019" />
<input type="hidden" name="search_code" id="search_code" value="true" />
<script>
  gl.projectOptions = gl.projectOptions || {};
  gl.projectOptions["advanced_bioinformatics"] = {
    issuesPath: "/witje010/advanced_bioinformatics/issues",
    mrPath: "/witje010/advanced_bioinformatics/merge_requests",
    name: "advanced_bioinformatics"
  };
</script>
<script>
  gl.dashboardOptions = {
    issuesPath: "https://git.wur.nl/dashboard/issues",
    mrPath: "https://git.wur.nl/dashboard/merge_requests"
  };
</script>
<input type="hidden" name="repository_ref" id="repository_ref" value="master" />

<div class="search-autocomplete-opts hide" data-autocomplete-path="/search/autocomplete" data-autocomplete-project-id="1019" data-autocomplete-project-ref="master"></div>
</form></div>

</li>
<li class="visible-sm visible-xs">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search"><i class="fa fa-search"></i>
</a></li>
<li>
<div>
<a class="btn btn-sign-in btn-success" href="/users/sign_in?redirect_to_referer=yes">Sign in</a>
</div>
</li>
</ul>
</div>
<h1 class="title"><a href="/u/witje010">Witjes, Lotte</a> / <a class="project-item-select-holder" href="/witje010/advanced_bioinformatics">advanced_bioinformatics</a></h1>
<div class="header-logo">
<a class="home" title="Dashboard" id="logo" href="/"><svg width="36" height="36" class="tanuki-logo">
  <path class="tanuki-shape tanuki-left-ear" fill="#e24329" d="M2 14l9.38 9v-9l-4-12.28c-.205-.632-1.176-.632-1.38 0z"/>
  <path class="tanuki-shape tanuki-right-ear" fill="#e24329" d="M34 14l-9.38 9v-9l4-12.28c.205-.632 1.176-.632 1.38 0z"/>
  <path class="tanuki-shape tanuki-nose" fill="#e24329" d="M18,34.38 3,14 33,14 Z"/>
  <path class="tanuki-shape tanuki-left-eye" fill="#fc6d26" d="M18,34.38 11.38,14 2,14 6,25Z"/>
  <path class="tanuki-shape tanuki-right-eye" fill="#fc6d26" d="M18,34.38 24.62,14 34,14 30,25Z"/>
  <path class="tanuki-shape tanuki-left-cheek" fill="#fca326" d="M2 14L.1 20.16c-.18.565 0 1.2.5 1.56l17.42 12.66z"/>
  <path class="tanuki-shape tanuki-right-cheek" fill="#fca326" d="M34 14l1.9 6.16c.18.565 0 1.2-.5 1.56L18 34.38z"/>
</svg>

</a></div>
<div class="js-dropdown-menu-projects">
<div class="dropdown-menu dropdown-select dropdown-menu-projects">
<div class="dropdown-title"><span>Go to a project</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search your projects" autocomplete="off" /><i class="fa fa-search dropdown-input-search"></i><i role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i class="fa fa-spinner fa-spin"></i></div>
</div>
</div>

</div>
</div>
</header>

<script>
  var findFileURL = "/witje010/advanced_bioinformatics/find_file/master";
</script>

<div class="page-with-sidebar">
<div class="sidebar-wrapper nicescroll">
<div class="sidebar-action-buttons">
<a class="nav-header-btn toggle-nav-collapse" title="Open/Close" href="#"><span class="sr-only">Toggle navigation</span>
<i class="fa fa-bars"></i>
</a><a class="nav-header-btn pin-nav-btn has-tooltip  js-nav-pin" title="Pin Navigation" data-placement="right" data-container="body" href="#"><span class="sr-only">Toggle navigation pinning</span>
<i class="fa fa-fw fa-thumb-tack"></i>
</a></div>
<ul class="nav nav-sidebar">
<li class="home"><a title="Projects" href="/explore"><span>
Projects
</span>
</a></li><li class=""><a title="Groups" href="/explore/groups"><span>
Groups
</span>
</a></li><li class=""><a title="Snippets" href="/explore/snippets"><span>
Snippets
</span>
</a></li><li class=""><a title="Help" href="/help"><span>
Help
</span>
</a></li></ul>

</div>
<div class="layout-nav">
<div class="container-fluid">
<div class="scrolling-tabs-container">
<div class="fade-left">
<i class="fa fa-angle-left"></i>
</div>
<div class="fade-right">
<i class="fa fa-angle-right"></i>
</div>
<ul class="nav-links scrolling-tabs">
<li class="home"><a title="Project" class="shortcuts-project" href="/witje010/advanced_bioinformatics"><span>
Project
</span>
</a></li><li class=""><a title="Activity" class="shortcuts-project-activity" href="/witje010/advanced_bioinformatics/activity"><span>
Activity
</span>
</a></li><li class="active"><a title="Repository" class="shortcuts-tree" href="/witje010/advanced_bioinformatics/tree/master"><span>
Repository
</span>
</a></li><li class=""><a title="Graphs" class="shortcuts-graphs" href="/witje010/advanced_bioinformatics/graphs/master"><span>
Graphs
</span>
</a></li><li class="hidden">
<a title="Network" class="shortcuts-network" href="/witje010/advanced_bioinformatics/network/master">Network
</a></li>
<li class="hidden">
<a class="shortcuts-new-issue" href="/witje010/advanced_bioinformatics/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a title="Commits" class="shortcuts-commits" href="/witje010/advanced_bioinformatics/commits/master">Commits
</a></li>
<li class="hidden">
<a title="Issue Boards" class="shortcuts-issue-boards" href="/witje010/advanced_bioinformatics/board">Issue Boards</a>
</li>
</ul>
</div>

</div>
</div>
<div class="content-wrapper page-with-layout-nav">


<div class="flash-container flash-container-page">
</div>


<div class=" ">
<div class="content">
<div class="scrolling-tabs-container sub-nav-scroll">
<div class="fade-left">
<i class="fa fa-angle-left"></i>
</div>
<div class="fade-right">
<i class="fa fa-angle-right"></i>
</div>

<div class="nav-links sub-nav scrolling-tabs">
<ul class="container-fluid container-limited">
<li class="active"><a href="/witje010/advanced_bioinformatics/tree/master">Files
</a></li><li class=""><a href="/witje010/advanced_bioinformatics/commits/master">Commits
</a></li><li class=""><a href="/witje010/advanced_bioinformatics/network/master">Network
</a></li><li class=""><a href="/witje010/advanced_bioinformatics/compare?from=master&amp;to=master">Compare
</a></li><li class=""><a href="/witje010/advanced_bioinformatics/branches">Branches
</a></li><li class=""><a href="/witje010/advanced_bioinformatics/tags">Tags
</a></li></ul>
</div>
</div>

<div class="container-fluid container-limited">

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/witje010/advanced_bioinformatics/refs/switch" accept-charset="UTF-8" method="get"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="destination" id="destination" value="blob" />
<input type="hidden" name="path" id="path" value="exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="master" data-ref="master" data-refs-url="/witje010/advanced_bioinformatics/refs" data-field-name="ref" data-submit-form-on-click="true"><span class="dropdown-toggle-text">master</span><i class="fa fa-chevron-down"></i></button>
<div class="dropdown-menu dropdown-menu-selectable">
<div class="dropdown-title"><span>Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close" aria-label="Close" type="button"><i class="fa fa-times dropdown-menu-close-icon"></i></button></div>
<div class="dropdown-input"><input type="search" id="" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><i class="fa fa-search dropdown-input-search"></i><i role="button" class="fa fa-times dropdown-input-clear js-dropdown-input-clear"></i></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><i class="fa fa-spinner fa-spin"></i></div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li>
<a href="/witje010/advanced_bioinformatics/tree/master">advanced_bioinformatics
</a></li>
<li>
<a href="/witje010/advanced_bioinformatics/tree/master/exercise_P5">exercise_P5</a>
</li>
<li>
<a href="/witje010/advanced_bioinformatics/blob/master/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py"><strong>
tmp_26994-exercise_P5_lottewitjes-146...
</strong>
</a></li>
</ul>
</div>
<ul class="blob-commit-info hidden-xs">
<li class="commit js-toggle-container" id="commit-b68573ab">
<a href="/u/witje010"><img class="avatar has-tooltip hidden-xs s36" alt="Witjes, Lotte&#39;s avatar" title="Witjes, Lotte" data-container="body" src="https://secure.gravatar.com/avatar/5a962e70a38b4e3384578bd3dbd3fada?s=72&amp;d=identicon" /></a>
<div class="commit-info-block">
<div class="commit-row-title">
<span class="item-title">
<a class="commit-row-message" href="/witje010/advanced_bioinformatics/commit/b68573ab163aae8d4fec12238cc3a684abd11096">v1 Needle parser</a>
<span class="commit-row-message visible-xs-inline">
&middot;
b68573ab
</span>
</span>
<div class="commit-actions hidden-xs">
<button class="btn btn-clipboard" data-toggle="tooltip" data-placement="bottom" data-container="body" data-clipboard-text="b68573ab163aae8d4fec12238cc3a684abd11096" type="button" title="Copy to Clipboard"><i class="fa fa-clipboard"></i></button>
<a class="commit-short-id btn btn-transparent" href="/witje010/advanced_bioinformatics/commit/b68573ab163aae8d4fec12238cc3a684abd11096">b68573ab</a>

</div>
</div>
<div class="commit-row-info">
<a class="commit-author-link has-tooltip" title="lotte.witjes@wur.nl" href="/u/witje010">Witjes, Lotte</a>
authored
<time class="js-timeago js-timeago-pending" datetime="2016-11-11T11:53:59Z" title="Nov 11, 2016 11:53am" data-toggle="tooltip" data-placement="top" data-container="body">2016-11-11 12:53:59 +0100</time><script>
//<![CDATA[
$('.js-timeago-pending').removeClass('js-timeago-pending').timeago()
//]]>
</script>
</div>
</div>
</li>

</ul>
<div class="blob-content-holder" id="blob-content-holder">
<article class="file-holder">
<div class="file-title">
<i class="fa fa-file-text-o fa-fw"></i>
<strong>
tmp_26994-exercise_P5_lottewitjes-1462136885.py
</strong>
<small>
5.62 KB
</small>
<div class="file-actions hidden-xs">
<div class="btn-group tree-btn-group">
<a class="btn btn-sm" target="_blank" href="/witje010/advanced_bioinformatics/raw/master/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py">Raw</a>
<a class="btn btn-sm" href="/witje010/advanced_bioinformatics/blame/master/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py">Blame</a>
<a class="btn btn-sm" href="/witje010/advanced_bioinformatics/commits/master/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py">History</a>
<a class="btn btn-sm" href="/witje010/advanced_bioinformatics/blob/b68573ab163aae8d4fec12238cc3a684abd11096/exercise_P5/tmp_26994-exercise_P5_lottewitjes-1462136885.py">Permalink</a>
</div>

</div>
</div>
<div class="file-content code js-syntax-highlight">
<div class="line-numbers">
<a class="diff-line-num" data-line-number="1" href="#L1" id="L1">
<i class="fa fa-link"></i>
1
</a>
<a class="diff-line-num" data-line-number="2" href="#L2" id="L2">
<i class="fa fa-link"></i>
2
</a>
<a class="diff-line-num" data-line-number="3" href="#L3" id="L3">
<i class="fa fa-link"></i>
3
</a>
<a class="diff-line-num" data-line-number="4" href="#L4" id="L4">
<i class="fa fa-link"></i>
4
</a>
<a class="diff-line-num" data-line-number="5" href="#L5" id="L5">
<i class="fa fa-link"></i>
5
</a>
<a class="diff-line-num" data-line-number="6" href="#L6" id="L6">
<i class="fa fa-link"></i>
6
</a>
<a class="diff-line-num" data-line-number="7" href="#L7" id="L7">
<i class="fa fa-link"></i>
7
</a>
<a class="diff-line-num" data-line-number="8" href="#L8" id="L8">
<i class="fa fa-link"></i>
8
</a>
<a class="diff-line-num" data-line-number="9" href="#L9" id="L9">
<i class="fa fa-link"></i>
9
</a>
<a class="diff-line-num" data-line-number="10" href="#L10" id="L10">
<i class="fa fa-link"></i>
10
</a>
<a class="diff-line-num" data-line-number="11" href="#L11" id="L11">
<i class="fa fa-link"></i>
11
</a>
<a class="diff-line-num" data-line-number="12" href="#L12" id="L12">
<i class="fa fa-link"></i>
12
</a>
<a class="diff-line-num" data-line-number="13" href="#L13" id="L13">
<i class="fa fa-link"></i>
13
</a>
<a class="diff-line-num" data-line-number="14" href="#L14" id="L14">
<i class="fa fa-link"></i>
14
</a>
<a class="diff-line-num" data-line-number="15" href="#L15" id="L15">
<i class="fa fa-link"></i>
15
</a>
<a class="diff-line-num" data-line-number="16" href="#L16" id="L16">
<i class="fa fa-link"></i>
16
</a>
<a class="diff-line-num" data-line-number="17" href="#L17" id="L17">
<i class="fa fa-link"></i>
17
</a>
<a class="diff-line-num" data-line-number="18" href="#L18" id="L18">
<i class="fa fa-link"></i>
18
</a>
<a class="diff-line-num" data-line-number="19" href="#L19" id="L19">
<i class="fa fa-link"></i>
19
</a>
<a class="diff-line-num" data-line-number="20" href="#L20" id="L20">
<i class="fa fa-link"></i>
20
</a>
<a class="diff-line-num" data-line-number="21" href="#L21" id="L21">
<i class="fa fa-link"></i>
21
</a>
<a class="diff-line-num" data-line-number="22" href="#L22" id="L22">
<i class="fa fa-link"></i>
22
</a>
<a class="diff-line-num" data-line-number="23" href="#L23" id="L23">
<i class="fa fa-link"></i>
23
</a>
<a class="diff-line-num" data-line-number="24" href="#L24" id="L24">
<i class="fa fa-link"></i>
24
</a>
<a class="diff-line-num" data-line-number="25" href="#L25" id="L25">
<i class="fa fa-link"></i>
25
</a>
<a class="diff-line-num" data-line-number="26" href="#L26" id="L26">
<i class="fa fa-link"></i>
26
</a>
<a class="diff-line-num" data-line-number="27" href="#L27" id="L27">
<i class="fa fa-link"></i>
27
</a>
<a class="diff-line-num" data-line-number="28" href="#L28" id="L28">
<i class="fa fa-link"></i>
28
</a>
<a class="diff-line-num" data-line-number="29" href="#L29" id="L29">
<i class="fa fa-link"></i>
29
</a>
<a class="diff-line-num" data-line-number="30" href="#L30" id="L30">
<i class="fa fa-link"></i>
30
</a>
<a class="diff-line-num" data-line-number="31" href="#L31" id="L31">
<i class="fa fa-link"></i>
31
</a>
<a class="diff-line-num" data-line-number="32" href="#L32" id="L32">
<i class="fa fa-link"></i>
32
</a>
<a class="diff-line-num" data-line-number="33" href="#L33" id="L33">
<i class="fa fa-link"></i>
33
</a>
<a class="diff-line-num" data-line-number="34" href="#L34" id="L34">
<i class="fa fa-link"></i>
34
</a>
<a class="diff-line-num" data-line-number="35" href="#L35" id="L35">
<i class="fa fa-link"></i>
35
</a>
<a class="diff-line-num" data-line-number="36" href="#L36" id="L36">
<i class="fa fa-link"></i>
36
</a>
<a class="diff-line-num" data-line-number="37" href="#L37" id="L37">
<i class="fa fa-link"></i>
37
</a>
<a class="diff-line-num" data-line-number="38" href="#L38" id="L38">
<i class="fa fa-link"></i>
38
</a>
<a class="diff-line-num" data-line-number="39" href="#L39" id="L39">
<i class="fa fa-link"></i>
39
</a>
<a class="diff-line-num" data-line-number="40" href="#L40" id="L40">
<i class="fa fa-link"></i>
40
</a>
<a class="diff-line-num" data-line-number="41" href="#L41" id="L41">
<i class="fa fa-link"></i>
41
</a>
<a class="diff-line-num" data-line-number="42" href="#L42" id="L42">
<i class="fa fa-link"></i>
42
</a>
<a class="diff-line-num" data-line-number="43" href="#L43" id="L43">
<i class="fa fa-link"></i>
43
</a>
<a class="diff-line-num" data-line-number="44" href="#L44" id="L44">
<i class="fa fa-link"></i>
44
</a>
<a class="diff-line-num" data-line-number="45" href="#L45" id="L45">
<i class="fa fa-link"></i>
45
</a>
<a class="diff-line-num" data-line-number="46" href="#L46" id="L46">
<i class="fa fa-link"></i>
46
</a>
<a class="diff-line-num" data-line-number="47" href="#L47" id="L47">
<i class="fa fa-link"></i>
47
</a>
<a class="diff-line-num" data-line-number="48" href="#L48" id="L48">
<i class="fa fa-link"></i>
48
</a>
<a class="diff-line-num" data-line-number="49" href="#L49" id="L49">
<i class="fa fa-link"></i>
49
</a>
<a class="diff-line-num" data-line-number="50" href="#L50" id="L50">
<i class="fa fa-link"></i>
50
</a>
<a class="diff-line-num" data-line-number="51" href="#L51" id="L51">
<i class="fa fa-link"></i>
51
</a>
<a class="diff-line-num" data-line-number="52" href="#L52" id="L52">
<i class="fa fa-link"></i>
52
</a>
<a class="diff-line-num" data-line-number="53" href="#L53" id="L53">
<i class="fa fa-link"></i>
53
</a>
<a class="diff-line-num" data-line-number="54" href="#L54" id="L54">
<i class="fa fa-link"></i>
54
</a>
<a class="diff-line-num" data-line-number="55" href="#L55" id="L55">
<i class="fa fa-link"></i>
55
</a>
<a class="diff-line-num" data-line-number="56" href="#L56" id="L56">
<i class="fa fa-link"></i>
56
</a>
<a class="diff-line-num" data-line-number="57" href="#L57" id="L57">
<i class="fa fa-link"></i>
57
</a>
<a class="diff-line-num" data-line-number="58" href="#L58" id="L58">
<i class="fa fa-link"></i>
58
</a>
<a class="diff-line-num" data-line-number="59" href="#L59" id="L59">
<i class="fa fa-link"></i>
59
</a>
<a class="diff-line-num" data-line-number="60" href="#L60" id="L60">
<i class="fa fa-link"></i>
60
</a>
<a class="diff-line-num" data-line-number="61" href="#L61" id="L61">
<i class="fa fa-link"></i>
61
</a>
<a class="diff-line-num" data-line-number="62" href="#L62" id="L62">
<i class="fa fa-link"></i>
62
</a>
<a class="diff-line-num" data-line-number="63" href="#L63" id="L63">
<i class="fa fa-link"></i>
63
</a>
<a class="diff-line-num" data-line-number="64" href="#L64" id="L64">
<i class="fa fa-link"></i>
64
</a>
<a class="diff-line-num" data-line-number="65" href="#L65" id="L65">
<i class="fa fa-link"></i>
65
</a>
<a class="diff-line-num" data-line-number="66" href="#L66" id="L66">
<i class="fa fa-link"></i>
66
</a>
<a class="diff-line-num" data-line-number="67" href="#L67" id="L67">
<i class="fa fa-link"></i>
67
</a>
<a class="diff-line-num" data-line-number="68" href="#L68" id="L68">
<i class="fa fa-link"></i>
68
</a>
<a class="diff-line-num" data-line-number="69" href="#L69" id="L69">
<i class="fa fa-link"></i>
69
</a>
<a class="diff-line-num" data-line-number="70" href="#L70" id="L70">
<i class="fa fa-link"></i>
70
</a>
<a class="diff-line-num" data-line-number="71" href="#L71" id="L71">
<i class="fa fa-link"></i>
71
</a>
<a class="diff-line-num" data-line-number="72" href="#L72" id="L72">
<i class="fa fa-link"></i>
72
</a>
<a class="diff-line-num" data-line-number="73" href="#L73" id="L73">
<i class="fa fa-link"></i>
73
</a>
<a class="diff-line-num" data-line-number="74" href="#L74" id="L74">
<i class="fa fa-link"></i>
74
</a>
<a class="diff-line-num" data-line-number="75" href="#L75" id="L75">
<i class="fa fa-link"></i>
75
</a>
<a class="diff-line-num" data-line-number="76" href="#L76" id="L76">
<i class="fa fa-link"></i>
76
</a>
<a class="diff-line-num" data-line-number="77" href="#L77" id="L77">
<i class="fa fa-link"></i>
77
</a>
<a class="diff-line-num" data-line-number="78" href="#L78" id="L78">
<i class="fa fa-link"></i>
78
</a>
<a class="diff-line-num" data-line-number="79" href="#L79" id="L79">
<i class="fa fa-link"></i>
79
</a>
<a class="diff-line-num" data-line-number="80" href="#L80" id="L80">
<i class="fa fa-link"></i>
80
</a>
<a class="diff-line-num" data-line-number="81" href="#L81" id="L81">
<i class="fa fa-link"></i>
81
</a>
<a class="diff-line-num" data-line-number="82" href="#L82" id="L82">
<i class="fa fa-link"></i>
82
</a>
<a class="diff-line-num" data-line-number="83" href="#L83" id="L83">
<i class="fa fa-link"></i>
83
</a>
<a class="diff-line-num" data-line-number="84" href="#L84" id="L84">
<i class="fa fa-link"></i>
84
</a>
<a class="diff-line-num" data-line-number="85" href="#L85" id="L85">
<i class="fa fa-link"></i>
85
</a>
<a class="diff-line-num" data-line-number="86" href="#L86" id="L86">
<i class="fa fa-link"></i>
86
</a>
<a class="diff-line-num" data-line-number="87" href="#L87" id="L87">
<i class="fa fa-link"></i>
87
</a>
<a class="diff-line-num" data-line-number="88" href="#L88" id="L88">
<i class="fa fa-link"></i>
88
</a>
<a class="diff-line-num" data-line-number="89" href="#L89" id="L89">
<i class="fa fa-link"></i>
89
</a>
<a class="diff-line-num" data-line-number="90" href="#L90" id="L90">
<i class="fa fa-link"></i>
90
</a>
<a class="diff-line-num" data-line-number="91" href="#L91" id="L91">
<i class="fa fa-link"></i>
91
</a>
<a class="diff-line-num" data-line-number="92" href="#L92" id="L92">
<i class="fa fa-link"></i>
92
</a>
<a class="diff-line-num" data-line-number="93" href="#L93" id="L93">
<i class="fa fa-link"></i>
93
</a>
<a class="diff-line-num" data-line-number="94" href="#L94" id="L94">
<i class="fa fa-link"></i>
94
</a>
<a class="diff-line-num" data-line-number="95" href="#L95" id="L95">
<i class="fa fa-link"></i>
95
</a>
<a class="diff-line-num" data-line-number="96" href="#L96" id="L96">
<i class="fa fa-link"></i>
96
</a>
<a class="diff-line-num" data-line-number="97" href="#L97" id="L97">
<i class="fa fa-link"></i>
97
</a>
<a class="diff-line-num" data-line-number="98" href="#L98" id="L98">
<i class="fa fa-link"></i>
98
</a>
<a class="diff-line-num" data-line-number="99" href="#L99" id="L99">
<i class="fa fa-link"></i>
99
</a>
<a class="diff-line-num" data-line-number="100" href="#L100" id="L100">
<i class="fa fa-link"></i>
100
</a>
<a class="diff-line-num" data-line-number="101" href="#L101" id="L101">
<i class="fa fa-link"></i>
101
</a>
<a class="diff-line-num" data-line-number="102" href="#L102" id="L102">
<i class="fa fa-link"></i>
102
</a>
<a class="diff-line-num" data-line-number="103" href="#L103" id="L103">
<i class="fa fa-link"></i>
103
</a>
<a class="diff-line-num" data-line-number="104" href="#L104" id="L104">
<i class="fa fa-link"></i>
104
</a>
<a class="diff-line-num" data-line-number="105" href="#L105" id="L105">
<i class="fa fa-link"></i>
105
</a>
<a class="diff-line-num" data-line-number="106" href="#L106" id="L106">
<i class="fa fa-link"></i>
106
</a>
<a class="diff-line-num" data-line-number="107" href="#L107" id="L107">
<i class="fa fa-link"></i>
107
</a>
<a class="diff-line-num" data-line-number="108" href="#L108" id="L108">
<i class="fa fa-link"></i>
108
</a>
<a class="diff-line-num" data-line-number="109" href="#L109" id="L109">
<i class="fa fa-link"></i>
109
</a>
<a class="diff-line-num" data-line-number="110" href="#L110" id="L110">
<i class="fa fa-link"></i>
110
</a>
<a class="diff-line-num" data-line-number="111" href="#L111" id="L111">
<i class="fa fa-link"></i>
111
</a>
<a class="diff-line-num" data-line-number="112" href="#L112" id="L112">
<i class="fa fa-link"></i>
112
</a>
<a class="diff-line-num" data-line-number="113" href="#L113" id="L113">
<i class="fa fa-link"></i>
113
</a>
<a class="diff-line-num" data-line-number="114" href="#L114" id="L114">
<i class="fa fa-link"></i>
114
</a>
<a class="diff-line-num" data-line-number="115" href="#L115" id="L115">
<i class="fa fa-link"></i>
115
</a>
<a class="diff-line-num" data-line-number="116" href="#L116" id="L116">
<i class="fa fa-link"></i>
116
</a>
<a class="diff-line-num" data-line-number="117" href="#L117" id="L117">
<i class="fa fa-link"></i>
117
</a>
<a class="diff-line-num" data-line-number="118" href="#L118" id="L118">
<i class="fa fa-link"></i>
118
</a>
<a class="diff-line-num" data-line-number="119" href="#L119" id="L119">
<i class="fa fa-link"></i>
119
</a>
<a class="diff-line-num" data-line-number="120" href="#L120" id="L120">
<i class="fa fa-link"></i>
120
</a>
<a class="diff-line-num" data-line-number="121" href="#L121" id="L121">
<i class="fa fa-link"></i>
121
</a>
<a class="diff-line-num" data-line-number="122" href="#L122" id="L122">
<i class="fa fa-link"></i>
122
</a>
<a class="diff-line-num" data-line-number="123" href="#L123" id="L123">
<i class="fa fa-link"></i>
123
</a>
<a class="diff-line-num" data-line-number="124" href="#L124" id="L124">
<i class="fa fa-link"></i>
124
</a>
<a class="diff-line-num" data-line-number="125" href="#L125" id="L125">
<i class="fa fa-link"></i>
125
</a>
<a class="diff-line-num" data-line-number="126" href="#L126" id="L126">
<i class="fa fa-link"></i>
126
</a>
<a class="diff-line-num" data-line-number="127" href="#L127" id="L127">
<i class="fa fa-link"></i>
127
</a>
<a class="diff-line-num" data-line-number="128" href="#L128" id="L128">
<i class="fa fa-link"></i>
128
</a>
<a class="diff-line-num" data-line-number="129" href="#L129" id="L129">
<i class="fa fa-link"></i>
129
</a>
<a class="diff-line-num" data-line-number="130" href="#L130" id="L130">
<i class="fa fa-link"></i>
130
</a>
<a class="diff-line-num" data-line-number="131" href="#L131" id="L131">
<i class="fa fa-link"></i>
131
</a>
<a class="diff-line-num" data-line-number="132" href="#L132" id="L132">
<i class="fa fa-link"></i>
132
</a>
<a class="diff-line-num" data-line-number="133" href="#L133" id="L133">
<i class="fa fa-link"></i>
133
</a>
<a class="diff-line-num" data-line-number="134" href="#L134" id="L134">
<i class="fa fa-link"></i>
134
</a>
<a class="diff-line-num" data-line-number="135" href="#L135" id="L135">
<i class="fa fa-link"></i>
135
</a>
<a class="diff-line-num" data-line-number="136" href="#L136" id="L136">
<i class="fa fa-link"></i>
136
</a>
<a class="diff-line-num" data-line-number="137" href="#L137" id="L137">
<i class="fa fa-link"></i>
137
</a>
<a class="diff-line-num" data-line-number="138" href="#L138" id="L138">
<i class="fa fa-link"></i>
138
</a>
<a class="diff-line-num" data-line-number="139" href="#L139" id="L139">
<i class="fa fa-link"></i>
139
</a>
<a class="diff-line-num" data-line-number="140" href="#L140" id="L140">
<i class="fa fa-link"></i>
140
</a>
<a class="diff-line-num" data-line-number="141" href="#L141" id="L141">
<i class="fa fa-link"></i>
141
</a>
<a class="diff-line-num" data-line-number="142" href="#L142" id="L142">
<i class="fa fa-link"></i>
142
</a>
<a class="diff-line-num" data-line-number="143" href="#L143" id="L143">
<i class="fa fa-link"></i>
143
</a>
<a class="diff-line-num" data-line-number="144" href="#L144" id="L144">
<i class="fa fa-link"></i>
144
</a>
<a class="diff-line-num" data-line-number="145" href="#L145" id="L145">
<i class="fa fa-link"></i>
145
</a>
</div>
<div class="blob-content" data-blob-id="49374582effc403302ff1d7d69cd27dd800208fa">
<pre class="code highlight"><code><span id="LC1" class="line"><span class="kn">from</span> <span class="nn">__future__</span> <span class="kn">import</span> <span class="n">division</span></span>
<span id="LC2" class="line"></span>
<span id="LC3" class="line"><span class="c">#!/usr/bin/evn python</span></span>
<span id="LC4" class="line"><span class="s">"""</span></span>
<span id="LC5" class="line"><span class="s">Author: Lotte Witjes</span></span>
<span id="LC6" class="line"><span class="s">Student number: 950405 966 120</span></span>
<span id="LC7" class="line"></span>
<span id="LC8" class="line"><span class="s">A script that parses the output of Needle alignment between a reference sequence and (multiple) related sequences and prints a summary table on the screen.</span></span>
<span id="LC9" class="line"><span class="s">The script contains a function that calculates the Hamming distance between two sequences of EQUAL length, it doesn't work for sequences of unequal length (will give error).</span></span>
<span id="LC10" class="line"><span class="s">The script contains a function that calculates the percentage identity between two sequences. If the sequences are of unequal length, please define the Hamming distance as parameter.</span></span>
<span id="LC11" class="line"></span>
<span id="LC12" class="line"><span class="s">Run the script from the command line as follows:</span></span>
<span id="LC13" class="line"><span class="s">$ python exercise_P5_lottewitjes.py (your reference fasta) (your related fasta)</span></span>
<span id="LC14" class="line"></span>
<span id="LC15" class="line"><span class="s">The script produces one output file, which is the output file of the Needle alignment, containing all alignments that had been performed. The file is called 'out.needle'.</span></span>
<span id="LC16" class="line"><span class="s">"""</span></span>
<span id="LC17" class="line"></span>
<span id="LC18" class="line"><span class="kn">from</span> <span class="nn">sys</span> <span class="kn">import</span> <span class="n">argv</span></span>
<span id="LC19" class="line"><span class="kn">import</span> <span class="nn">subprocess</span></span>
<span id="LC20" class="line"><span class="kn">import</span> <span class="nn">os.path</span></span>
<span id="LC21" class="line"></span>
<span id="LC22" class="line"><span class="k">def</span> <span class="nf">fastaparser</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></span>
<span id="LC23" class="line">	<span class="s">"""Parses a .fasta file into a dictionary where keys are accessions codes and values are the actual sequences."""</span></span>
<span id="LC24" class="line">	<span class="n">thefile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="s">"r"</span><span class="p">)</span></span>
<span id="LC25" class="line">	<span class="n">seqs</span> <span class="o">=</span> <span class="p">{}</span></span>
<span id="LC26" class="line">	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">thefile</span><span class="p">:</span></span>
<span id="LC27" class="line">		<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">"&gt;"</span><span class="p">):</span></span>
<span id="LC28" class="line">			<span class="n">label</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">"&gt;"</span><span class="p">,</span> <span class="s">""</span><span class="p">)</span></span>
<span id="LC29" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">label</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></span>
<span id="LC30" class="line">			<span class="n">seqs</span><span class="p">[</span><span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC31" class="line">		<span class="k">else</span><span class="p">:</span></span>
<span id="LC32" class="line">			<span class="n">seqs</span><span class="p">[</span><span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="o">+=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span>
<span id="LC33" class="line">	</span>
<span id="LC34" class="line">	<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">seqs</span><span class="p">:</span></span>
<span id="LC35" class="line">		<span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="s">""</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">])]</span></span>
<span id="LC36" class="line">	</span>
<span id="LC37" class="line">	<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">seqs</span><span class="p">:</span></span>
<span id="LC38" class="line">		<span class="k">if</span> <span class="s">"|"</span> <span class="ow">in</span> <span class="n">key</span><span class="p">:</span></span>
<span id="LC39" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">key</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">"|"</span><span class="p">)</span></span>
<span id="LC40" class="line">			<span class="n">seqs</span><span class="p">[</span><span class="n">elements</span><span class="p">[</span><span class="mi">2</span><span class="p">]]</span> <span class="o">=</span> <span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span>
<span id="LC41" class="line">			<span class="k">del</span> <span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span>
<span id="LC42" class="line">	<span class="k">return</span> <span class="n">seqs</span></span>
<span id="LC43" class="line"></span>
<span id="LC44" class="line"><span class="k">def</span> <span class="nf">determineSequenceLengths</span><span class="p">(</span><span class="n">filename</span><span class="p">):</span></span>
<span id="LC45" class="line">	<span class="s">"""Returns the dictionary as in the function fastaparser but now the length of the sequence is added in the values of the keys."""</span></span>
<span id="LC46" class="line">	<span class="n">seqs</span> <span class="o">=</span> <span class="n">fastaparser</span><span class="p">(</span><span class="n">filename</span><span class="p">)</span></span>
<span id="LC47" class="line">	<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">seqs</span><span class="p">:</span></span>
<span id="LC48" class="line">		<span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span></span>
<span id="LC49" class="line">		<span class="n">seqs</span><span class="p">[</span><span class="n">key</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">length</span><span class="p">)</span></span>
<span id="LC50" class="line">	<span class="k">return</span> <span class="n">seqs</span></span>
<span id="LC51" class="line"></span>
<span id="LC52" class="line"><span class="k">def</span> <span class="nf">runNeedle</span><span class="p">(</span><span class="n">inputReference</span><span class="p">,</span> <span class="n">inputRelated</span><span class="p">,</span> <span class="n">gapopen</span><span class="p">,</span> <span class="n">gapextend</span><span class="p">):</span></span>
<span id="LC53" class="line">	<span class="s">"""Runs Needle alignment with sequence1, versus sequence2, with defined gapopen and gapextend values. The output is always out.needle.</span></span>
<span id="LC54" class="line"><span class="s">	The program checks if this output file already exists, if it does than Needle isn't executed."""</span></span>
<span id="LC55" class="line">	<span class="n">output</span> <span class="o">=</span> <span class="s">"out.needle"</span></span>
<span id="LC56" class="line">	<span class="n">cmd</span> <span class="o">=</span> <span class="s">"needle -asequence {0} -bsequence {1} -gapopen {2} -gapextend {3} -outfile {4}"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">inputReference</span><span class="p">,</span> <span class="n">inputRelated</span><span class="p">,</span> <span class="n">gapopen</span><span class="p">,</span> <span class="n">gapextend</span><span class="p">,</span> <span class="n">output</span><span class="p">)</span></span>
<span id="LC57" class="line">	<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">output</span><span class="p">):</span></span>
<span id="LC58" class="line">		<span class="k">pass</span></span>
<span id="LC59" class="line">	<span class="k">else</span><span class="p">:</span></span>
<span id="LC60" class="line">		<span class="n">e</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">shell</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></span>
<span id="LC61" class="line">		<span class="n">res</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_call</span><span class="p">(</span><span class="n">cmd</span><span class="p">,</span> <span class="n">shell</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span></span>
<span id="LC62" class="line">		<span class="k">return</span> <span class="n">res</span></span>
<span id="LC63" class="line"></span>
<span id="LC64" class="line"><span class="k">def</span> <span class="nf">hammingDistance</span><span class="p">(</span><span class="n">sequence1</span><span class="p">,</span> <span class="n">sequence2</span><span class="p">):</span></span>
<span id="LC65" class="line">	<span class="s">"""Returns the number of different amino acids/bases between two sequences of equal length"""</span></span>
<span id="LC66" class="line">	<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence1</span><span class="p">)</span> <span class="o">==</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence2</span><span class="p">):</span></span>
<span id="LC67" class="line">		<span class="n">difference</span> <span class="o">=</span> <span class="mi">0</span></span>
<span id="LC68" class="line">		<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">sequence1</span><span class="p">)):</span></span>
<span id="LC69" class="line">			<span class="k">if</span> <span class="n">sequence1</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">!=</span> <span class="n">sequence2</span><span class="p">[</span><span class="n">i</span><span class="p">]:</span></span>
<span id="LC70" class="line">				<span class="n">difference</span> <span class="o">+=</span> <span class="mi">1</span></span>
<span id="LC71" class="line">	<span class="k">return</span> <span class="n">differences</span></span>
<span id="LC72" class="line"></span>
<span id="LC73" class="line"><span class="k">def</span> <span class="nf">percentageIdentity</span><span class="p">(</span><span class="n">sequence1</span><span class="p">,</span> <span class="n">sequence2</span><span class="p">,</span> <span class="n">alignmentLength</span><span class="p">,</span> <span class="n">hamming</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span>
<span id="LC74" class="line">	<span class="s">"""Returns the percentage identity between two sequences of equal length or different length. If sequences of different length, define Hamming distance. </span></span>
<span id="LC75" class="line"><span class="s">	The percentage identity is defined as identical amino acids or bases divided by the alignment length times 100."""</span></span>
<span id="LC76" class="line">	<span class="k">if</span> <span class="n">hamming</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span></span>
<span id="LC77" class="line">		<span class="n">hamming</span> <span class="o">=</span> <span class="n">hammingDistance</span><span class="p">(</span><span class="n">sequence1</span><span class="p">,</span> <span class="n">sequence2</span><span class="p">)</span></span>
<span id="LC78" class="line">		<span class="n">numberOfIdenticalPositions</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence1</span><span class="p">)</span> <span class="o">-</span> <span class="nb">float</span><span class="p">(</span><span class="n">hamming</span><span class="p">)</span></span>
<span id="LC79" class="line">		<span class="n">percentOfIdentity</span> <span class="o">=</span> <span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">numberOfIdenticalPositions</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="n">alignmentLength</span><span class="p">))</span><span class="o">*</span><span class="mi">100</span></span>
<span id="LC80" class="line">	<span class="k">else</span><span class="p">:</span></span>
<span id="LC81" class="line">		<span class="n">numberOfIdenticalPositions</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">sequence1</span><span class="p">)</span> <span class="o">-</span> <span class="nb">float</span><span class="p">(</span><span class="n">hamming</span><span class="p">)</span></span>
<span id="LC82" class="line">		<span class="n">percentOfIdentity</span> <span class="o">=</span> <span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">numberOfIdenticalPositions</span><span class="p">)</span> <span class="o">/</span> <span class="nb">float</span><span class="p">(</span><span class="n">alignmentLength</span><span class="p">))</span><span class="o">*</span><span class="mi">100</span></span>
<span id="LC83" class="line">	<span class="k">return</span> <span class="n">percentOfIdentity</span></span>
<span id="LC84" class="line"></span>
<span id="LC85" class="line"><span class="k">def</span> <span class="nf">parseNeedleIDs</span><span class="p">(</span><span class="n">output</span><span class="p">):</span></span>
<span id="LC86" class="line">	<span class="s">"""Parses the IDs of the Needle output into a list in the same order as the output."""</span></span>
<span id="LC87" class="line">	<span class="n">thefile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="s">"r"</span><span class="p">)</span></span>
<span id="LC88" class="line">	<span class="n">infoNeedleIDs</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC89" class="line">	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">thefile</span><span class="p">:</span></span>
<span id="LC90" class="line">		<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">"# 2:"</span><span class="p">):</span></span>
<span id="LC91" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></span>
<span id="LC92" class="line">			<span class="n">infoNeedleIDs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elements</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span></span>
<span id="LC93" class="line">	<span class="k">return</span> <span class="n">infoNeedleIDs</span></span>
<span id="LC94" class="line"></span>
<span id="LC95" class="line"></span>
<span id="LC96" class="line"><span class="k">def</span> <span class="nf">parseNeedleHamming</span><span class="p">(</span><span class="n">output</span><span class="p">):</span></span>
<span id="LC97" class="line">	<span class="s">"""Parses the Hamming distance of the Needle output into a list in the same order as the output."""</span></span>
<span id="LC98" class="line">	<span class="n">thefile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="s">"r"</span><span class="p">)</span></span>
<span id="LC99" class="line">	<span class="n">infoNeedleSimilarity</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC100" class="line">	<span class="n">infoNeedleLength</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC101" class="line">	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">thefile</span><span class="p">:</span></span>
<span id="LC102" class="line">		<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">"# Similarity:"</span><span class="p">):</span></span>
<span id="LC103" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></span>
<span id="LC104" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">"/"</span><span class="p">)</span></span>
<span id="LC105" class="line">			<span class="n">infoNeedleSimilarity</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elements</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span>
<span id="LC106" class="line">			<span class="n">infoNeedleLength</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">elements</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></span>
<span id="LC107" class="line">	<span class="n">infoNeedleHamming</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC108" class="line">	<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">infoNeedleLength</span><span class="p">)):</span></span>
<span id="LC109" class="line">		<span class="n">hamming</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">infoNeedleLength</span><span class="p">[</span><span class="n">i</span><span class="p">])</span> <span class="o">-</span> <span class="nb">int</span><span class="p">(</span><span class="n">infoNeedleSimilarity</span><span class="p">[</span><span class="n">i</span><span class="p">])</span></span>
<span id="LC110" class="line">		<span class="n">infoNeedleHamming</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">hamming</span><span class="p">)</span></span>
<span id="LC111" class="line">	<span class="k">return</span> <span class="n">infoNeedleHamming</span></span>
<span id="LC112" class="line">	</span>
<span id="LC113" class="line"><span class="k">def</span> <span class="nf">parseNeedleIdentity</span><span class="p">(</span><span class="n">output</span><span class="p">):</span></span>
<span id="LC114" class="line">	<span class="s">"""Parses the percentage identities of the Needle output into a list in the same order as the output."""</span></span>
<span id="LC115" class="line">	<span class="n">thefile</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="s">"r"</span><span class="p">)</span></span>
<span id="LC116" class="line">	<span class="n">infoNeedleIdentity</span> <span class="o">=</span> <span class="p">[]</span></span>
<span id="LC117" class="line">	<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">thefile</span><span class="p">:</span></span>
<span id="LC118" class="line">		<span class="k">if</span> <span class="n">line</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">"# Identity:"</span><span class="p">):</span></span>
<span id="LC119" class="line">			<span class="n">elements</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">()</span></span>
<span id="LC120" class="line">			<span class="n">identity</span> <span class="o">=</span> <span class="n">elements</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span></span>
<span id="LC121" class="line">			<span class="n">identity</span> <span class="o">=</span> <span class="n">identity</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span></span>
<span id="LC122" class="line">			<span class="n">infoNeedleIdentity</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">identity</span><span class="p">)</span></span>
<span id="LC123" class="line">	<span class="k">return</span> <span class="n">infoNeedleIdentity</span></span>
<span id="LC124" class="line"></span>
<span id="LC125" class="line"><span class="k">def</span> <span class="nf">writeOutput</span><span class="p">(</span><span class="n">referenceSeqs</span><span class="p">,</span> <span class="n">relatedSeqs</span><span class="p">,</span> <span class="n">IDs</span><span class="p">,</span> <span class="n">hamming</span><span class="p">,</span> <span class="n">identity</span><span class="p">):</span></span>
<span id="LC126" class="line">	<span class="s">"""Writes a summary of the Needle output on the screen. Showing the ID and length of sequence1 and sequence2, the Hamming distance, and the percentage identity."""</span></span>
<span id="LC127" class="line">	<span class="k">print</span> <span class="s">"Sequence1	Length	Sequence2	Length	Hamm	Ident"</span></span>
<span id="LC128" class="line">	<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">IDs</span><span class="p">)):</span></span>
<span id="LC129" class="line">		<span class="n">line</span> <span class="o">=</span> <span class="s">"{0}	{1}	{2}	{3}	{4}	{5}"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="s">"GPA1_ARATH"</span><span class="p">,</span> <span class="n">referenceSeqs</span><span class="p">[</span><span class="s">"GPA1_ARATH"</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span> <span class="n">IDs</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">relatedSeqs</span><span class="p">[</span><span class="n">IDs</span><span class="p">[</span><span class="n">i</span><span class="p">]][</span><span class="mi">1</span><span class="p">],</span> <span class="n">hamming</span><span class="p">[</span><span class="n">i</span><span class="p">],</span> <span class="n">identity</span><span class="p">[</span><span class="n">i</span><span class="p">])</span></span>
<span id="LC130" class="line">		<span class="k">print</span> <span class="n">line</span></span>
<span id="LC131" class="line">		</span>
<span id="LC132" class="line"></span>
<span id="LC133" class="line"><span class="k">if</span>  <span class="n">__name__</span> <span class="o">==</span> <span class="s">"__main__"</span><span class="p">:</span></span>
<span id="LC134" class="line">	<span class="n">inputReference</span> <span class="o">=</span> <span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></span>
<span id="LC135" class="line">	<span class="n">inputRelated</span> <span class="o">=</span> <span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span></span>
<span id="LC136" class="line">	<span class="n">output</span> <span class="o">=</span> <span class="s">"out.needle"</span></span>
<span id="LC137" class="line">	<span class="n">referenceSeqs</span> <span class="o">=</span> <span class="n">determineSequenceLengths</span><span class="p">(</span><span class="n">inputReference</span><span class="p">)</span></span>
<span id="LC138" class="line">	<span class="n">relatedSeqs</span> <span class="o">=</span> <span class="n">determineSequenceLengths</span><span class="p">(</span><span class="n">inputRelated</span><span class="p">)</span></span>
<span id="LC139" class="line">			</span>
<span id="LC140" class="line">	<span class="n">runNeedle</span><span class="p">(</span><span class="n">inputReference</span><span class="p">,</span> <span class="n">inputRelated</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mf">0.5</span><span class="p">)</span></span>
<span id="LC141" class="line"></span>
<span id="LC142" class="line">	<span class="n">IDs</span> <span class="o">=</span> <span class="n">parseNeedleIDs</span><span class="p">(</span><span class="n">output</span><span class="p">)</span></span>
<span id="LC143" class="line">	<span class="n">hamming</span> <span class="o">=</span> <span class="n">parseNeedleHamming</span><span class="p">(</span><span class="n">output</span><span class="p">)</span></span>
<span id="LC144" class="line">	<span class="n">identity</span> <span class="o">=</span> <span class="n">parseNeedleIdentity</span><span class="p">(</span><span class="n">output</span><span class="p">)</span></span>
<span id="LC145" class="line">	<span class="n">writeOutput</span><span class="p">(</span><span class="n">referenceSeqs</span><span class="p">,</span> <span class="n">relatedSeqs</span><span class="p">,</span> <span class="n">IDs</span><span class="p">,</span> <span class="n">hamming</span><span class="p">,</span> <span class="n">identity</span><span class="p">)</span></span></code></pre>
</div>
</div>


</article>
</div>

</div>
</div>

</div>
</div>
</div>
</div>



</body>
</html>

