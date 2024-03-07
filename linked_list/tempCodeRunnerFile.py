
        current = self.head
        while current.next:
            
            val = current.data
            runner = current
            while runner.next != None:
                if runner.next.data == val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next