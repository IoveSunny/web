#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;
typedef struct node{
	ElemType data;
	int length;
	struct node *next;
} LinkNode, *LinkList;

void InitList(LinkList &L) {
	L = (LinkList)malloc(sizeof(LinkNode));
	L->length = 0;
	L->next = NULL;
}

void InsertList(LinkList &L, ElemType e) {
	LinkList p = L;
	p->length += 1;
	LinkList q = (LinkList)malloc(sizeof(LinkNode));
	q->data = e;
	
	q->next = p->next;
	p->next = q;

}

void DeleteList(LinkList &L, ElemType e) {
	LinkList pre,cur;
	if(L->next == NULL) {
		printf("LinkList is empty.\n");
		return ;
	}

	for(pre=L, cur=L->next; cur; pre=cur, cur=cur->next) {
		if(cur->data == e) {
			L->length -= 1;
			pre->next = cur->next;
			return ;
		}
	}

	printf("ElemType %c Doesn't Exist.\n", e);
}

void display(LinkList L) {
	LinkList p = L->next;
	if(!p) {
		printf("Empty.\n");
		return ;
	}
	while(p) {
		printf("%c ", p->data);
		p = p->next;
	}
	printf("\n");
}

void destroy(LinkList &L) {
	LinkList p = L, q;
	while(p) {
		q = p->next;
		free(p);
		p = q;
	}
}

void menu() {
	printf("1.Insert\n2.Delete\n3.Display\n0.Exit\n");
}

int main(void) {
	int choice;
	ElemType e;
	LinkList L;
	InitList(L);
	menu();


	while(1) {
		printf("Please Enter your choice: ");
		scanf("%d", &choice);
		getchar();
		
		switch(choice) {
			case 1:
				printf("Please Insert Elem: ");
				scanf("%c", &e);
				getchar();
				InsertList(L, e);
				break;
			case 2:
				printf("Please Delete Elem: ");
				scanf("%c", &e);
				getchar();
				DeleteList(L, e);
				break;
			case 3:
				printf("LinkList Elems: ");
				display(L);
				break;
			case 0:
				return 0;
			default:
				printf("Input Error.");
				break;
		}
	}
	
	destroy(L);

	return 0;
}