## Shippings - `/shippings/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  Anonymous |  `/shippings/` | `GET`|  `json` |  `200` |
|  Anonymous |  `/shippings/:id` | `GET`|  `json` |  `200`, `404` |
	


### DETAIL
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

- Add the shipping id to the URL: /shippings/:id/

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  shipping id |
|  `status`|  str | `PROCESSING`, `SUCCESS` or `FAIL` |
|  `order` | int  |  related order id |
|  `shipped_at` | datetime  |  creation timestamp |

#### Example

**Event**: Anonymous `GET` to `/shippings/1/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: `None`
```
```
**HTTP Status Code**: `200`  
**Response Content**:
```
{
  "id": 1,
  "order": 1,
  "shipped_at": "2020-05-06T19:22:52.633078Z",
  "status": 2
}
```

### LIST
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

- None

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  order id |
|  `status`|  str | 1 (`PROCESSING`), 2 (`SUCCESS`) or 3 (`FAIL`) |
|  `order` | int  |  related order id |
|  `shipped_at` | datetime  |  creation timestamp |

#### Example

**Event**: Anonymous `GET` to `/shippings/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: `None`
```
```
**HTTP Status Code**: `200`  
**Response Content**:
```
[
  {
    "id": 1,
    "order": 1,
    "shipped_at": "2020-05-06T19:22:52.633078Z",
    "status": PROCESSING"
  }
  {
    "id": 1,
    "order": 1,
    "shipped_at": "2020-05-06T19:23:52.633078Z",
    "status": PROCESSING"
  }
]
```