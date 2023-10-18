# Create user ============================================
'''

# create --> user_one
mutation {
  createUser(username:"user_one") {
    success
    user {
      userId
      username
    }
  }
}

# create --> user_two
mutation {
  createUser(username:"user_two") {
    success
    user {
      userId
      username
    }
  }
}

'''

# Query User By user_id ==============================================
"""
query {
  userId(username:"user_one")
}
"""


# create Message =====================================================
"""
mutation {
  createMessage(
    senderId: "1",
    recipientId: "2",
    content:"Hello there"
  ) {
    success
    message {
      content
      recipientId
      senderId
    }
  }
}
"""

# Subscription Message ===============================================