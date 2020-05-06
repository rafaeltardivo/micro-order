## Orders - `/orders/`


| Permission level  |   URL| Method  | Format   |  HTTP Status Code |
|---|---|---|---|---|
|  Anonymous |  `/orders/` |   `GET`, `POST`|  `json` |  `201` |  
|  Anonymous |  `/orders/:id` |  `GET`|  `json` |  `200`, `404` |  

### CREATE
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

|  Field | Type  | Required  |  Min Length |  Max Length |  Detail |
|---|---|---|---|---|---|
| `customer` |  int |  yes |  1 |  7 |  Customer unique identification |

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  order id |
|  `status`|  str |  `PROCESSING`, `SHIPPED` or `CANCELLED` |
|  `customer` | int  |  related customer id |
|  `made_at` | datetime  |  creation timestamp |

#### Example

**Event**: Anonymous `POST` to `/orders/`  
**Header Content**:
```
Content-Type: application/json
```
**Body Content**: 
```

{
	"customer": "1"
}

```
**HTTP Status Code**: `201`  
**Response Content**:
```
{
    "id": 1,
    "status": "PROCESSING",
    "customer": 1,
    "made_at": "2020-05-06T17:27:21.241132Z"
}
```

#### Validations
**HTTP Status Code**: `400`  

| Field  | Content  |  Detail |
|---|---|---|
| `customer`  |  Must be greater then 0. |  Customer id must be greater than 0 |

### DETAIL
** Permission required **: None

#### Headers
|  Field | Content  |
|---|---|
|  Content-Type | application/json  |

#### Request Content

- Add the order id to the URL: /orders/:id/

#### Response Content
|  Field | Type  |Detail   |
|---|---|---|
|  `id` | int  |  order id |
|  `status`|  str |  `PROCESSING`, `SHIPPED` or `CANCELLED` |
|  `customer` | int  |  related customer id |
|  `made_at` | datetime  |  creation timestamp |

#### Example

**Event**: Anonymous `GET` to `/orders/1/`  
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
    "status": "PROCESSING",
    "customer": 1,
    "made_at": "2020-05-06T17:27:21.241132Z"
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
|  `status`|  str |`PROCESSING`, `SHIPPED` or `CANCELLED`|
|  `customer` | int  |  related customer id |
|  `made_at` | datetime  |  creation timestamp |

#### Example

**Event**: Anonymous `GET` to `/orders/`  
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
    "status": "PROCESSING",
    "customer": 1,
    "made_at": "2020-05-06T17:18:49.118929Z"
  },
  {
    "id": 2,
    "status": "PROCESSING",
    "customer": 1,
    "made_at": "2020-05-06T17:19:06.068675Z"
  }
]
```