[help](https://www.twilio.com/blog/graphql-api-subscriptions-python-asyncio-ariadne)

```
async def hello_world():
    return "Hello world"
```



- We can call `asynchronous` functions in 3 ways:

- `asyncio.run`

- `asyncio.create_task`

- sing the `await` keyword
- Using `await`, we would call our `asynchronous` function as follows:

- `greeting = await hello_world()` 
- We will use the third approach throughout the article. It is important to note that we can only use await inside an asynchronous function.


