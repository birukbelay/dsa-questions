

public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    ListNode prehead = new ListNode(-1);
    ListNode cur = prehead;

    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            cur.next = l1;
            l1 = l1.next;
        } else {
            cur.next = l2;
            l2 = l2.next;
        }
        cur = cur.next;
    }

    cur.next = l1 == null ? l2 : l1;
    return prehead.next;
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ArrayList<Integer> arr=new ArrayList<>();
        ListNode ptr1=list1;
        ListNode ptr2=list2;

        while(ptr1!=null){
            arr.add(ptr1.val);
            ptr1=ptr1.next;
        }
        while(ptr2!=null){
            arr.add(ptr2.val);
            ptr2=ptr2.next;
        }
        
        Collections.sort(arr);

        ListNode res=new ListNode();
        if(arr.size()==0) return null;
        res.val=arr.get(0);
        if(arr.size()==1) return res;
        res.next=new ListNode();
        ListNode ptr=res;
        for(int i=1; i<arr.size(); i++){
            ListNode newNode=new ListNode();
            ptr.next=newNode;
            ptr.next.val=arr.get(i);
            ptr=ptr.next;
        }
        ptr=null;
        return res;
    }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode list = new ListNode();
        ListNode head = list;
        while(list1!=null && list2!=null){
            if(list1.val>list2.val){
                list.next=list2;
                list2 = list2.next;
            }
            else{
                list.next = list1;
                list1 = list1.next;
            }
            list = list.next;
        }
        while(list1!=null){
            list.next = list1;
            list1 = list1.next;
            list = list.next;
        }
        while(list2!=null){
            list.next = list2;
            list2 = list2.next;
            list = list.next;
        }
        list.next = null;
        return head.next;
    }
}

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        if(list1==null) return list2;
        else if(list2==null) return list1;
        ListNode res=new ListNode();
        ListNode ptr1=list1;
        ListNode ptr2=list2;

        if(ptr1.val>ptr2.val){
            res= ptr2;
            ptr2=ptr2.next;
        }else{
            res= ptr1;
            ptr1=ptr1.next;
        }
        ListNode resPtr=res;

        while(ptr1!=null && ptr2!=null){
            if(ptr1.val>ptr2.val){
                resPtr.next= ptr2;
                resPtr=resPtr.next;
                ptr2=ptr2.next;
            }else{
                resPtr.next= ptr1;
                resPtr=resPtr.next;
                ptr1=ptr1.next;
            }
        }

        if(ptr1==null) resPtr.next=ptr2;
        else resPtr.next= ptr1;
        return res;
    }
}