/* global $ location django */

$(document).ready(function () {
  var $main = $('main')
  var currentPath
  var popup
  var patternsForPopup = /\/accounts\b/
  var $top = $('<div tabindex="-1">')

  window.adhocracy4.getCurrentPath = function () {
    return currentPath
  }

  var headers = {
    'X-Embed': ''
  }

  var testCanSetCookie = function () {
    var cookie = 'can-set-cookie=true;'
    var regExp = new RegExp(cookie)
    document.cookie = cookie
    return regExp.test(document.cookie)
  }

  var createAlert = function (text, state, timeout) {
    var $alert = $('<p class="alert alert--' + state + ' alert--small" role="alert">' + text + '</p>')
    var $close = $('<button class="alert__close"><i class="fa fa-times"></i></button>')

    $alert.append($close)
    $close.attr('title', django.gettext('Close'))
    $close.find('i').attr('aria-label', django.gettext('Close'))

    var removeMessage = function () {
      $alert.remove()
    }
    $alert.on('click', removeMessage)
    if (typeof timeout === 'number') {
      setTimeout(removeMessage, timeout)
    }
    $alert.prependTo($('#embed-status'))
  }

  var extractScripts = function ($root, selector, attr) {
    var $existingValues = $('head').find(selector).map((i, e) => $(e).attr(attr))

    $root.find(selector).each(function (i, script) {
      var $script = $(script)
      if ($existingValues.filter((i, v) => v === $script.attr(attr)).length) {
        $script.remove()
      } else {
        $('head').append($script)
      }
    })
  }

  var loadHtml = function (html, textStatus, xhr) {
    var $root = $('<div>').html(html)
    var nextPath = xhr.getResponseHeader('x-ajax-path')
    var isInitial = !currentPath

    if (patternsForPopup.test(nextPath)) {
      $('#embed-confirm').modal('show')
      return false
    }
    // only update the currentPath if there was no modal opened
    currentPath = nextPath

    extractScripts($root, 'script[src]', 'src')
    extractScripts($root, 'link[rel="stylesheet"]', 'href')

    $main.empty()
    $main.append($top)
    $main.append($root.find('main').children())
    $(document).trigger('a4.embed.ready')
    $(window.init_widgets)
    // jump to top after navigation, but not on inital load
    if (!isInitial) {
      $top.focus()
    }
  }

  var onAjaxError = function (jqxhr) {
    var text
    switch (jqxhr.status) {
      case 404:
        text = django.gettext('We couldn\'t find what you were looking for.')
        break
      case 401:
      case 403:
        text = django.gettext('You don\'t have the permission to view this page.')
        break
      default:
        text = django.gettext('Something went wrong!')
        break
    }

    createAlert(text, 'danger', 6000)
  }

  var getEmbedTarget = function ($element, href) {
    var embedTarget = $element.data('embedTarget')

    if (embedTarget) {
      return embedTarget
    } else if (!href || href[0] === '#' || $element.attr('target')) {
      return 'ignore'
    } else if ($element.is('.rich-text a')) {
      return 'external'
    } else if (patternsForPopup.test(href)) {
      return 'popup'
    } else {
      return 'internal'
    }
  }

  $(document).on('click', 'a[href]', function (event) {
    // NOTE: event.target.href is resolved against /embed/
    var href = event.target.getAttribute('href')
    var $link = $(event.target)
    var embedTarget = getEmbedTarget($link, href)

    if (embedTarget === 'internal') {
      event.preventDefault()

      if (href[0] === '?') {
        href = currentPath + href
      }

      $.ajax({
        url: href,
        headers: headers,
        success: loadHtml,
        error: onAjaxError
      })
    } else if (embedTarget === 'popup') {
      event.preventDefault()
      popup = window.open(
        href,
        'embed_popup',
        'height=650,width=500,location=yes,menubar=no,toolbar=no,status=no'
      )
    }
  })

  $(document).on('submit', 'form[action]', function (event) {
    var form = event.target
    var $form = $(form)
    var embedTarget = getEmbedTarget($form, form.method)

    if (embedTarget === 'internal') {
      event.preventDefault()

      $.ajax({
        url: form.action,
        method: form.method,
        headers: headers,
        data: $form.serialize(),
        success: loadHtml,
        error: onAjaxError
      })
    }
  })

  $('.js-embed-logout').on('click', function (e) {
    e.preventDefault()
    $.post(
      '/accounts/logout/',
      function () {
        location.reload()
      }
    )
  })

  // The popup will send a message when the user is logged in. Only after
  // this message the Popup will close.
  window.addEventListener('message', function (e) {
    if (e.origin === location.origin) {
      // Browser extensions might use onmessage too, so catch any exceptions
      try {
        var data = JSON.parse(e.data)

        if (data.name === 'popup-close' && popup) {
          popup.close()
          location.reload()
        }
      } catch (e) {
      }
    }
  }, false)

  if (testCanSetCookie() === false) {
    var text = django.gettext('You have third party cookies disabled. You can still view the content of this project but won\'t be able to login.')
    createAlert(text, 'info')
  }

  $.ajax({
    url: $('body').data('url'),
    headers: headers,
    success: loadHtml,
    error: onAjaxError
  })
})
