from telemanager.database import *
master_id = 0

class AuthenticationCheck(object):
    """
    Simple authentication checkage to use the bot.
    This is intented to block unknown people posting/uploading data into
    bot folder, ensuring only rightfull data will be disposable.
    """
    def __init__(self, id):
        self.requested_id = id

    def _get_members(self):
        """
        Execute the query and return the list of results.
        """
        db.controller.execute(t4.search("USER_ID", self.requested_id))
        return db.controller.get()

    def check(self):
        """
        Perform master id and member table checkage
        """
        results = self.get_members()
        if self.requested_id not masted_id and len(results) == 0:
            return -1
        return 0
