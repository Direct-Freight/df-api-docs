# Direct Freight OpenAPI Specification
[![Build Status](https://travis-ci.org/Direct-Freight/df-api-docs.svg?branch=master)](https://travis-ci.org/Direct-Freight/df-api-docs)


## Links

- Documentation: http://apidocs.directfreight.com/
- SwaggerUI: http://apidocs.directfreight.com/swagger-ui/
- Look at full spec:
    + JSON http://apidocs.directfreight.com/swagger.json
    + YAML http://apidocs.directfreight.com/swagger.yaml
- Preview spec version for branch `[branch]`: https://docs.directfreight.com/preview/[branch]

## Editing specification with swagger-editor
### Install

1. Install [Node JS](https://nodejs.org/)
2. Clone repo and `cd`
    + Run `npm install`

### Usage

1. Run `npm start`
2. Checkout console output to see where local server is started. You can use all [links](#links) (except `preview`) by replacing https://direct-freight.github.io/df-api-docs/ with url from the message: `Server started <url>`
3. Make changes using your favorite editor or `swagger-editor` (look for URL in console output)
4. All changes are immediately propagated to your local server, moreover all documentation pages will be automagically refreshed in a browser after each change
**TIP:** you can open `swagger-editor`, documentation and `swagger-ui` in parallel
5. Once you finish with the changes you can run tests using: `npm test`
6. Share you changes with the rest of the world by pushing to GitHub :smile:

### Steps to finish

1. **[Optional]** You can setup [custom domain](https://help.github.com/articles/using-a-custom-domain-with-github-pages/) (just create `web/CNAME` file)
2. **[Optional]** If you document public API consider adding it into [APIs.guru](https://APIs.guru) directory using [this form](https://apis.guru/add-api/).
