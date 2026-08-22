---
title: "Get the list of sprints tasks.api.scrum.sprint.list | Bitrix24 REST API and Marketplace Applications"
source: "https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-list.html"
author:
published:
created: 2026-02-13
description:
tags:
  - "clippings"
---
> Scope: [`task`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/scopes/permissions.html)
> 
> Who can execute the method: any user

The method `tasks.api.scrum.sprint.list` returns a list of sprints.

This method is similar to other methods with filtering by list.

## Method parameters

| **Name**   `type` | **Description** |
| --- | --- |
| **order**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | An object for sorting the result. The object format is `{'sorting_field': 'sorting_direction' [, ...]}`. Available fields are described in the table [below](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-list.html#fields).  Sorting direction can take the following values:  - `asc` — ascending - `desc` — descending |
| **filter**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | An object in the format `{'filter_field': 'filter_value' [, ...]}`. Available fields are described in the table [below](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-list.html#fields) |
| **select**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | An array of record fields that will be returned by the method. You can specify only the fields that are necessary.  If the array contains the value `"*"`, all available fields will be returned.  The default value is an empty array `array()`. In this case, all fields of the main query table will be returned |
| **start**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | The page number of the output. Works for https requests |

### Available filter fields

| **Name**   `type` | **Description** |
| --- | --- |
| **ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint identifier |
| **GROUP\_ID**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Scrum identifier |
| **ENTITY\_TYPE**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Entity type |
| **NAME**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Name |
| **SORT**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sorting |
| **CREATED\_BY**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Created by |
| **MODIFIED\_BY**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Modified by |
| **DATE\_START**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Start date |
| **DATE\_END**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | End date |
| **STATUS**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Status |
| **INFO**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Information |

## Code examples

[How to Use Examples in Documentation](https://apidocs.bitrix24.com/first-steps/how-to-use-examples.html)

cURL (Webhook)

cURL (oAuth)

JS

PHP

BX24.js

PHP CRest

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
"filter": {
    "GROUP_ID": 1,
    ">=DATE_END": "2024-07-19T15:03:01+00:00"
}
}' \
https://your-domain.bitrix24.com/rest/_USER_ID_/_CODE_/tasks.api.scrum.sprint.list
```

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{
"filter": {
    "GROUP_ID": 1,
    ">=DATE_END": "2024-07-19T15:03:01+00:00"
},
"auth": "YOUR_ACCESS_TOKEN"
}' \
https://your-domain.bitrix24.com/rest/tasks.api.scrum.sprint.list
```

```js
// callListMethod is recommended when you need to retrieve the entire set of list data and the volume of records is relatively small (up to about 1000 items). The method loads all data at once, which can lead to high memory load when working with large volumes.

const groupId = 1;
try {
  const response = await $b24.callListMethod(
    'tasks.api.scrum.sprint.list',
    {
      filter: {
        GROUP_ID: groupId,
        '>=DATE_END': new Date()
      }
    },
    (progress) => { console.log('Progress:', progress) }
  );
  const items = response.getData() || [];
  for (const entity of items) { console.log('Entity:', entity); }
} catch (error) {
  console.error('Request failed', error);
}

// fetchListMethod is preferable when working with large datasets. The method implements iterative fetching using a generator, allowing data to be processed in parts and efficiently using memory.

const groupId = 1;
try {
  const generator = $b24.fetchListMethod('tasks.api.scrum.sprint.list', {
    filter: {
      GROUP_ID: groupId,
      '>=DATE_END': new Date()
    }
  }, 'ID');
  for await (const page of generator) {
    for (const entity of page) { console.log('Entity:', entity); }
  }
} catch (error) {
  console.error('Request failed', error);
}

// callMethod provides manual control over the pagination process through the start parameter. Suitable for scenarios where precise control over request batches is required. However, with large volumes of data, it may be less efficient compared to fetchListMethod.

const groupId = 1;
try {
  const response = await $b24.callMethod('tasks.api.scrum.sprint.list', {
    filter: {
      GROUP_ID: groupId,
      '>=DATE_END': new Date()
    }
  }, 0);
  const result = response.getData().result || [];
  for (const entity of result) { console.log('Entity:', entity); }
} catch (error) {
  console.error('Request failed', error);
}
```

```js
const groupId = 1;
BX24.callMethod(
    'tasks.api.scrum.sprint.list',
    {
        filter: {
            GROUP_ID: groupId,
            '>=DATE_END': new Date()
        }
    },
    function(res)
    {
        console.log(res);
    }
);
```

```php
require_once('crest.php'); // include CRest PHP SDK

// execute a request to the REST API
$result = CRest::call(
    'tasks.api.scrum.sprint.list',
    [
        'filter' => [
            'GROUP_ID' => 1,
            '>=DATE_END' => '2024-07-19T15:03:01+00:00'
        ]
    ]
);

// Process the response from Bitrix24
if (isset($result['error'])) {
    echo 'Error: '.$result['error_description'];
} else {
    print_r($result['result']);
}
```

## Response handling

HTTP status: **200**

```json
[
    {
        "id": 2,
        "groupId": 143,
        "entityType": "sprint",
        "name": "Sprint 1",
        "goal": "",
        "sort": 1,
        "createdBy": 1,
        "modifiedBy": 1,
        "dateStart": "2024-07-19T15:03:01+00:00",
        "dateEnd": "2024-08-02T15:03:01+00:00",
        "status": "planned"
    },
    {
        "id": 3,
        "groupId": 1,
        "entityType": "sprint",
        "name": "Sprint 1",
        "goal": "",
        "sort": 1,
        "createdBy": 1,
        "modifiedBy": 1,
        "dateStart": "2021-11-21T22:00:00+00:00",
        "dateEnd": "2021-11-28T22:00:00+00:00",
        "status": "planned"
    }
]
```

### Returned data

| **Name**   `type` | **Description** |
| --- | --- |
| **result**   [`object`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | An object containing data about the sprint |
| **id**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sprint identifier |
| **groupId**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Identifier of the group (Scrum) to which the sprint belongs |
| **entityType**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Entity type (in this case `sprint`) |
| **name**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Name of the sprint |
| **goal**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Goal of the sprint. Set only in the interface when starting the sprint |
| **sort**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Sorting |
| **createdBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Identifier of the user who created the sprint |
| **modifiedBy**   [`integer`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Identifier of the user who modified the sprint |
| **dateStart**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Start date of the sprint in `ISO 8601` format |
| **dateEnd**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | End date of the sprint in `ISO 8601` format |
| **status**   [`string`](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/data-types.html) | Status of the sprint |

HTTP status: **400**

```json
{
    "error": 0,
    "error_description": "Could not load list"
}
```

| **Name**   `type` | **Description** |
| --- | --- |
| **error**   `string` | String error code. It may consist of digits, Latin letters, and underscores |
| **error\_description**   `error_description` | Textual description of the error. The description is not intended to be shown to the end user in its raw form |

| **Code** | **Error message** | **Description** |
| --- | --- | --- |
| `0` | `Could not load list` | No sprints found with the specified filters |

HTTP Status: **20x**, **40x**, **50x**

The errors described below may occur when calling any method.

| **Status** | **Code**   **Error Message** | **Description** |
| --- | --- | --- |
| `500` | `INTERNAL_SERVER_ERROR`   Internal server error | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `500` | `ERROR_UNEXPECTED_ANSWER`   Server returned an unexpected response | An internal server error has occurred, please contact the server administrator or [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `503` | `QUERY_LIMIT_EXCEEDED`   Too many requests | The [request intensity limit](https://apidocs.bitrix24.com/limits.html) has been exceeded |
| `405` | `ERROR_BATCH_METHOD_NOT_ALLOWED`   Method is not allowed for batch usage | The current method is not allowed to be called using [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) |
| `400` | `ERROR_BATCH_LENGTH_EXCEEDED`   Max batch length exceeded | The maximum length of parameters passed to the [batch](https://apidocs.bitrix24.com/settings/how-to-call-rest-api/batch.html) method has been exceeded |
| `401` | `NO_AUTH_FOUND`   Wrong authorization data | Invalid [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook code](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) |
| `400` | `INVALID_REQUEST`   Https required | The methods must be called using the HTTPS protocol |
| `503` | `OVERLOAD_LIMIT`   REST API is blocked due to overload | The REST API is blocked due to overload. This is a manual individual block, to remove it you need to contact [Bitrix24 technical support](https://apidocs.bitrix24.com/bitrix-support.html) |
| `403` | `ACCESS_DENIED`   REST API is available only on commercial plans | The REST API is available only on commercial plans |
| `403` | `INVALID_CREDENTIALS`   Invalid request credentials | The user whose [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) or [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) was used to call the method lacks permissions |
| `404` | `ERROR_MANIFEST_IS_NOT_AVAILABLE`   Manifest is not available | The manifest is not available |
| `403` | `insufficient_scope`   The request requires higher privileges than provided by the webhook token | The request requires higher privileges than those provided by the [webhook](https://apidocs.bitrix24.com/local-integrations/local-webhooks.html) token |
| `401` | `expired_token`   The access token provided has expired | The provided [access token](https://apidocs.bitrix24.com/settings/oauth/index.html) has expired |
| `403` | `user_access_error`   The user does not have access to the application | The user does not have access to the application. This means that the application is installed, but the account administrator has allowed access to this application only for specific users |
| `500` | `PORTAL_DELETED`   Portal was deleted | The public part of the site is closed. To open the public part of the site on an on-premise installation, disable the option "Temporary closure of the public part of the site". Path to the setting: *Desktop > Settings > Product Settings > Module Settings > Main Module > Temporary closure of the public part of the site* |

## Continue exploring

- [Add Sprint in Scrum tasks.api.scrum.sprint.add](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-add.html)
- [Update Sprint tasks.api.scrum.sprint.update](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-update.html)
- [Start Sprint tasks.api.scrum.sprint.start](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-start.html)
- [Complete the active sprint of the selected Scrum tasks.api.scrum.sprint.complete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-complete.html)
- [Get Sprint Fields by Its Identifier tasks.api.scrum.sprint.get](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-get.html)
- [Delete Sprint tasks.api.scrum.sprint.delete](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-delete.html)
- [Get a list of available fields for the sprint tasks.api.scrum.sprint.getFields](https://apidocs.bitrix24.com/api-reference/sonet-group/scrum/sprint/api-reference/sonet-group/scrum/sprint/tasks-api-scrum-sprint-get-fields.html)