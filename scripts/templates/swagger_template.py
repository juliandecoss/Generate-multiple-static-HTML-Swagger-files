TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Swagger UI</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700|Source+Code+Pro:300,600|Titillium+Web:400,600,700" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui.css" >
  <style>
    html
    {
      box-sizing: border-box;
      overflow: -moz-scrollbars-vertical;
      overflow-y: scroll;
    }
    *,
    *:before,
    *:after
    {
      box-sizing: inherit;
    }
    body {
      margin:0;
      background: #fafafa;
    }
  </style>
</head>
<body>
<div id="swagger-ui"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-bundle.js"> </script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/swagger-ui/3.43.0/swagger-ui-standalone-preset.js"> </script>
<form>
    <label for="select" style="position: absolute; left: 70rem; top: 8rem;">
        <span style="font-size: 16px; color: #3b4151;  font-family: sans-serif; margin-right: 15px; font-weight: 900;">Select a service</span>
        <select name="formal" onchange="javascript:handleSelect(this)" style="text-align: center; width: 20rem; background-color: #f7f7f7; height: 25px; border-color: #62a03f; border-radius: 5px; border-width: 2px;">
            <option>Options</option>
            <option value="pet">pet</option>
            <option value="callback">callback</option>
        </select>
            <script type="text/javascript">
              function handleSelect(elm)
              {window.location = elm.value+".html";}
            </script>
    </label>
</form>
<script>
window.onload = function() {
  var spec = %s;
  // Build a system
  const ui = SwaggerUIBundle({
    spec: spec,
    dom_id: '#swagger-ui',
    deepLinking: true,
    presets: [
      SwaggerUIBundle.presets.apis,
      SwaggerUIStandalonePreset
    ],
    plugins: [
      SwaggerUIBundle.plugins.DownloadUrl
    ],
    layout: "StandaloneLayout"
  })
  window.ui = ui
}
</script>
</body>
</html>
"""