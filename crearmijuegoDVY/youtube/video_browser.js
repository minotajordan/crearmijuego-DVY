var ytvb = {};
ytvb.MAX_RESULTS_LIST = 6;
ytvb.MAX_RESULTS_RELATED = 4;
ytvb.MAX_RESULTS_USER = 4;
ytvb.THUMBNAIL_WIDTH = 150;
ytvb.THUMBNAIL_HEIGHT = 100;
ytvb.PREVIOUS_PAGE_BUTTON = 'previousPageButton';
ytvb.NEXT_PAGE_BUTTON = 'nextPageButton';
ytvb.VIDEO_LIST_TABLE = 'searchResultsVideoListTable';
ytvb.VIDEO_LIST_TABLE_CONTAINER_DIV = 'searchResultsVideoList';
ytvb.VIDEO_PLAYER_DIV = 'videoPlayer';
ytvb.RELATED_VIDEOS_DIV = 'relatedVideos';
ytvb.USER_VIDEOS_DIV = 'userVideos';
ytvb.MAIN_SEARCH_CONTAINER_DIV = 'mainSearchBox';
ytvb.TOP_SEARCH_CONTAINER_DIV = 'searchBox';
ytvb.VIDEO_DESCRIPTION_CSS_CLASS = 'videoDescription';
ytvb.VIDEO_LIST_CSS_CLASS = 'videoList';
ytvb.RELATED_VIDEOS_REL = 'http://gdata.youtube.com/schemas/2007#video.related';
ytvb.FLASH_MIME_TYPE = 'application/x-shockwave-flash';
ytvb.STANDARD_FEED_URL_TOP_RATED = 'http://gdata.youtube.com/feeds/standardfeeds/top_rated';
ytvb.STANDARD_FEED_URL_MOST_VIEWED = 'http://gdata.youtube.com/feeds/standardfeeds/most_viewed';
ytvb.STANDARD_FEED_URL_RECENTLY_FEATURED = 'http://gdata.youtube.com/feeds/standardfeeds/recently_featured';
ytvb.VIDEO_FEED_URL = 'http://gdata.youtube.com/feeds/videos';
ytvb.QUERY_URL_MAP = {
  'top_rated' : ytvb.STANDARD_FEED_URL_TOP_RATED,
  'most_viewed' : ytvb.STANDARD_FEED_URL_MOST_VIEWED,
  'recently_featured' : ytvb.STANDARD_FEED_URL_RECENTLY_FEATURED,
  'all' : ytvb.VIDEO_FEED_URL
};
ytvb.USER_VIDEOS_SUFFIX = '/uploads';
ytvb.REFERRING_FEED_TYPE_MAIN = 'main';
ytvb.REFERRING_FEED_TYPE_RELATED = 'related';
ytvb.REFERRING_FEED_TYPE_USER = 'user';
ytvb.nextPage = 2;
ytvb.previousPage = 0;
ytvb.previousSearchTerm = '';
ytvb.previousQueryType = 'all';
ytvb.jsonFeed_ = null;
ytvb.jsonFeedRelated_ = null;
ytvb.jsonFeedUser_ = null;
ytvb.appendScriptTag = function(scriptSrc, scriptId, scriptCallback) {
  // Remove any old existance of a script tag by the same name
  var oldScriptTag = document.getElementById(scriptId);
  if (oldScriptTag) {
    oldScriptTag.parentNode.removeChild(oldScriptTag);
  }
  // Create new script tag
  var script = document.createElement('script');
  script.setAttribute('src', 
      scriptSrc + '&alt=json-in-script&callback=' + scriptCallback);
  script.setAttribute('id', scriptId);
  script.setAttribute('type', 'text/javascript');
  // Append the script tag to the head to retrieve a JSON feed of videos
  // NOTE: This requires that a head tag already exists in the DOM at the
  // time this function is executed.
  document.getElementsByTagName('head')[0].appendChild(script);
};

ytvb.findLinkHref = function(entry, rel) {
  for (var i = 0, link; link = entry.link[i]; i++) {
    if (link.rel == rel) {
      return link.href;
    }
  }
  // a link with the specified rel was not found
  return null;
};

ytvb.findMediaContentHref = function(entry, type) {
  for (var i = 0, content; content = entry.media$group.media$content[i]; i++) {
    if (content.type == type) {
      return content.url;
    }
  }
  // a media:content element with the specified MIME type was not found
  return null;
};

ytvb.listVideos = function(queryType, searchTerm, page) {
  ytvb.previousSearchTerm = searchTerm; 
  ytvb.previousQueryType = queryType; 
  var queryUrl = ytvb.QUERY_URL_MAP[queryType];
  if (queryUrl) {
    queryUrl += '?max-results=' + ytvb.MAX_RESULTS_LIST +
        '&start-index=' + (((page - 1) * ytvb.MAX_RESULTS_LIST) + 1);
    if (searchTerm != '') {
      queryUrl += '&vq=' + searchTerm;
    }
    ytvb.appendScriptTag(queryUrl, 
                         'searchResultsVideoListScript', 
                         'ytvb.listVideosCallback');
    ytvb.updateNavigation(page);
  } else {
    alert('Unknown feed type specified');
  }
};

ytvb.listVideosCallback = function(data) {
  // Stores the json data returned for later lookup by entry index value
  ytvb.jsonFeed_ = data.feed;
  var resultsTableContainer = document.getElementById(
      ytvb.VIDEO_LIST_TABLE_CONTAINER_DIV);

  // Deletes and re-adds the results table from container
  // NOTE: Any other elements added to the container will also be cleared
  while (resultsTableContainer.childNodes.length >= 1) {
    resultsTableContainer.removeChild(resultsTableContainer.firstChild);
  }

  var resultsTable = document.createElement('table');
  resultsTable.setAttribute('class', ytvb.VIDEO_LIST_CSS_CLASS);
  var tbody = document.createElement('tbody');
  resultsTable.setAttribute('width', '100%');
  resultsTableContainer.appendChild(resultsTable);

  // Loops through entries in the feed and calls appendVideoData for each
  for (var i = 0, entry; entry = data.feed.entry[i]; i++) {
    // The entry.yt$noembed property will exist if this YouTube video does
    // not support viewing in an embedded player on a third-party site.  
    // Exclude these videos from listing here.  A feature request has been
    // submitted for an additional query parameter to exclude these results
    // from the initial results feed.
    if (! entry.yt$noembed) {
      ytvb.appendVideoDataToTable(tbody, entry, i);
    }
  }
  resultsTable.appendChild(tbody);
};

ytvb.showRelatedVideos = function(entryIndex, referringFeed) {
  var entry;
  try {
    if (referringFeed == ytvb.REFERRING_FEED_TYPE_RELATED) {
      entry = ytvb.jsonFeedRelated_.entry[entryIndex];
    } else if (referringFeed == ytvb.REFERRING_FEED_TYPE_USER) {
      entry = ytvb.jsonFeedUser_.entry[entryIndex];
    } else if (referringFeed == ytvb.REFERRING_FEED_TYPE_MAIN) {
      entry = ytvb.jsonFeed_.entry[entryIndex];
    } else {
      throw "Unknown type of referring feed.";
    }
    var relatedHref = ytvb.findLinkHref(entry, ytvb.RELATED_VIDEOS_REL);
    var relatedVideosDiv = document.getElementById(ytvb.RELATED_VIDEOS_DIV);
    while (relatedVideosDiv.childNodes.length >= 1) {
      relatedVideosDiv.removeChild(relatedVideosDiv.firstChild);
    }
    relatedVideosDiv.innerHTML = '<b>Relacionados:</b><br />';
    if (relatedHref) {
      relatedHref += '?max-results=' + ytvb.MAX_RESULTS_RELATED;
      ytvb.appendScriptTag(relatedHref, 
          'showRelatedVideosScript', 
          'ytvb.showRelatedVideosCallback');
    }
  } catch (err) {
    alert(err);
  }
};

ytvb.showRelatedVideosCallback = function(data) {
  var relatedVideosDiv = document.getElementById(ytvb.RELATED_VIDEOS_DIV);
  ytvb.jsonFeedRelated_ = data.feed;
  for (var i= 0, entry; entry = data.feed.entry[i]; i++) {
    relatedVideosJson = entry; 
    var img = document.createElement('img');
    img.setAttribute('src', entry.media$group.media$thumbnail[0].url);
    img.onclick = ytvb.generatePlayVideoLinkOnclick(entry.id.$t, i, 
        ytvb.REFERRING_FEED_TYPE_RELATED);
    img.setAttribute('width', ytvb.THUMBNAIL_WIDTH);
    img.setAttribute('height', ytvb.THUMBNAIL_HEIGHT);
    relatedVideosDiv.appendChild(img);
  }
};

ytvb.showVideosByUser = function(userProfileUrl) {
  var userVideosDiv = document.getElementById(ytvb.USER_VIDEOS_DIV);
  while (userVideosDiv.childNodes.length >= 1) {
    userVideosDiv.removeChild(userVideosDiv.firstChild);
  }
  var queryUrl = userProfileUrl + ytvb.USER_VIDEOS_SUFFIX +
      '?max-results=' + ytvb.MAX_RESULTS_USER + 
      '&orderby=rating';
  userVideosDiv.innerHTML = '<br /><b>Los videos mas votados por el usuario:</b><br />';
  ytvb.appendScriptTag(queryUrl, 
      'showVideosByUserScript', 
      'ytvb.showVideosByUserCallback');
};

ytvb.showVideosByUserCallback = function(data) {
  var userVideosDiv = document.getElementById(ytvb.USER_VIDEOS_DIV);
  ytvb.jsonFeedUser_ = data.feed;
  for (var i = 0, entry; entry = data.feed.entry[i]; i++) {
    userVideosJson = entry;
    var img = document.createElement('img');
    img.setAttribute('src', entry.media$group.media$thumbnail[0].url);
    img.onclick = ytvb.generatePlayVideoLinkOnclick(entry.id.$t, i, 
        ytvb.REFERRING_FEED_TYPE_USER);
    img.setAttribute('width', ytvb.THUMBNAIL_WIDTH);
    img.setAttribute('height', ytvb.THUMBNAIL_HEIGHT);
    userVideosDiv.appendChild(img);
  }
};

ytvb.generatePlayVideoLinkOnclick = function(videoUrl, 
                                             entryIndex, 
                                             referringFeed) {
  return function() {
    ytvb.playVideo(entryIndex, referringFeed);
    return false;
  };
};

ytvb.appendVideoDataToTable = function(tbody, entry, entryIndex) {
  var tr = document.createElement('tr');
  tr.onclick = ytvb.generatePlayVideoLinkOnclick(entry.id.$t, entryIndex, 
      ytvb.REFERRING_FEED_TYPE_MAIN);


  var thumbnailTd = document.createElement('td');
  var thumbnailImage = document.createElement('img');
  thumbnailImage.setAttribute('src', entry.media$group.media$thumbnail[0].url);
  thumbnailImage.setAttribute('width', '100');

  thumbnailTd.appendChild(thumbnailImage);

  var metadataTd = document.createElement('td');
  metadataTd.setAttribute('width', '100%');
  var metadataLink = document.createElement('a');
  metadataLink.setAttribute('href', '#'); 
  metadataLink.innerHTML = entry.media$group.media$title.$t;
  var descPara = document.createElement('p');
  descPara.innerHTML = entry.media$group.media$description.$t;
  descPara.setAttribute('class', ytvb.VIDEO_DESCRIPTION_CSS_CLASS);
  metadataTd.appendChild(metadataLink);
  metadataTd.appendChild(descPara);

  tr.appendChild(thumbnailTd);
  tr.appendChild(metadataTd);
  tbody.appendChild(tr);
};

ytvb.playVideo = function(entryIndex, referringFeed) {
  var entry;
  try {
    if (referringFeed == ytvb.REFERRING_FEED_TYPE_RELATED) {
      entry = ytvb.jsonFeedRelated_.entry[entryIndex];
    } else if (referringFeed == ytvb.REFERRING_FEED_TYPE_USER) {
      entry = ytvb.jsonFeedUser_.entry[entryIndex];
    } else if (referringFeed == ytvb.REFERRING_FEED_TYPE_MAIN) {
      entry = ytvb.jsonFeed_.entry[entryIndex];
    } else {
      throw "Unknown type of referring feed.";
    }
    var videoHref = ytvb.findMediaContentHref(entry, ytvb.FLASH_MIME_TYPE);
    var videoPlayerDiv = document.getElementById(ytvb.VIDEO_PLAYER_DIV);
    var youvilink = videoHref.substring(25,36);
    var youvilinkinicio = 'https://www.youtube.com/watch?v='+youvilink;
    // Add standard YouTube video embed code, with standard height/width
    // values.  Enable autoplay of the video.
    var html = [];
    html.push('<div id="linkyoutube" value='+youvilinkinicio+'>'+entry.media$group.media$title.$t+'</div>');    
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');
    html.push('<br/>');    
    videoPlayerDiv.innerHTML = html.join('');
    ytvb.showRelatedVideos(entryIndex, referringFeed);
    if (entry.author && entry.author.length > 0) {
      ytvb.showVideosByUser(entry.author[0].uri.$t);
    }
  } catch (err) {
    alert(err);
  }
};

ytvb.updateNavigation = function(page) {
  ytvb.nextPage = page + 1;
  ytvb.previousPage = page - 1;
  document.getElementById(ytvb.NEXT_PAGE_BUTTON).style.display = 'inline';
  document.getElementById(ytvb.PREVIOUS_PAGE_BUTTON).style.display = 'inline';
  if (ytvb.previousPage < 1) {
    document.getElementById(ytvb.PREVIOUS_PAGE_BUTTON).disabled = true;
  } else {
    document.getElementById(ytvb.PREVIOUS_PAGE_BUTTON).disabled = false;
  }
  document.getElementById(ytvb.NEXT_PAGE_BUTTON).disabled = false;
};

ytvb.hideMainSearch = function() {
  document.getElementById(ytvb.MAIN_SEARCH_CONTAINER_DIV).style.display = 
      'none';
  document.getElementById(ytvb.TOP_SEARCH_CONTAINER_DIV).style.display = 
      'inline';
};

ytvb.queryTypeChanged = function(queryType, searchTermInputElement) {
  if (queryType != 'all') {
    searchTermInputElement.value = '';
  }
};

$(function(){
    $('.show-menu').click(function(e){
		e.stopPropagation();
	});
	$(document).click(function(){
		$('#main > .show-menu').show("slide", { direction: "right" }, 1000);
	});

    $("#function-menu").click(function(){
    	$(".show-menu").show("slide", { direction: "right" }, 1000);
    	return false;
    });	
});