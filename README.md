# Direct Freight OpenAPI Specification
[![Build Status](https://travis-ci.org/Direct-Freight/df-api-docs.svg?branch=master)](https://travis-ci.org/Direct-Freight/df-api-docs)

## Steps to finish

6. If you did everything correct, https://direct-freight.github.io/df-api-docs/ will lead to your new docs
7. **[Optional]** You can setup [custom domain](https://help.github.com/articles/using-a-custom-domain-with-github-pages/) (just create `web/CNAME` file)
8. Start writing/editing your OpenAPI spec: check out [usage](#usage) section below
9. **[Optional]** If you document public API consider adding it into [APIs.guru](https://APIs.guru) directory using [this form](https://apis.guru/add-api/).
10. Delete this section :smile:

## Links

- Documentation(ReDoc): https://direct-freight.github.io/df-api-docs/
- SwaggerUI: https://direct-freight.github.io/df-api-docs/swagger-ui/
- Look full spec:
    + JSON https://direct-freight.github.io/df-api-docs/swagger.json
    + YAML https://direct-freight.github.io/df-api-docs/swagger.yaml
- Preview spec version for branch `[branch]`: https://direct-freight.github.io/df-api-docs/preview/[branch]

**Warning:** All above links are updated only after Travis CI finishes deployment

## Working on specification
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
