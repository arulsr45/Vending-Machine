//
//  ViewController.m
//  Vending Machine
//
//  Created by Arul on 4/29/15.
//  Copyright (c) 2015 Arul . All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


// setting up the connection with the table in the cloud
-(instancetype)initWithCoder:(NSCoder *)aCoder{
    self = [super initWithCoder:aCoder];
    if(self){
        self.parseClassName = @"Object";
        self.textKey = @"title";
        self.pullToRefreshEnabled = YES;
    }
    
    return self;
}

// querying the table and setting up caching for faster UX
-(PFQuery *)queryForTable{
    PFQuery *query = [PFQuery queryWithClassName:self.parseClassName];
    [query orderByAscending:@"createdAt"];
    query.cachePolicy = kPFCachePolicyCacheThenNetwork;
    return query;
}


// filling out the table on the app with the information from the cloud
-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath object:(PFObject *)object{
    UITableViewCell *cell = [self.tableView dequeueReusableCellWithIdentifier:@"Cell" forIndexPath:indexPath];
    
    BOOL notificationSent = NO;
    
    NSString *item = [object objectForKey:@"title"];
    
    cell.textLabel.text = item;

    long obj = [[object objectForKey:@"quantity"] integerValue];
    
    if (obj <= 10 && notificationSent == NO) {
        notificationSent = YES;
        [self setLocalNotification:item];
    }
    cell.detailTextLabel.text = [[object objectForKey:@"quantity"] stringValue];
    
    
    return cell;
}

// setting up the notification in case of low stock
-(void)setLocalNotification:(NSString *)item{
    UIAlertController *alertUser = [UIAlertController alertControllerWithTitle:@"Low Stock Alert" message:[NSString stringWithFormat:@"You are running low on %@!",item] preferredStyle:UIAlertControllerStyleAlert];
    UIAlertAction *okayAction = [UIAlertAction actionWithTitle:@"OK" style:UIAlertActionStyleDefault handler:nil];
    [alertUser addAction:okayAction];

    [self presentViewController:alertUser animated:YES completion:nil];

    
    
}

@end
