#!/bin/bash
aws ec2 disassociate-address --association-id eipassoc-2eabea14
aws ec2 release-address --allocation-id eipalloc-a614719c
aws ec2 terminate-instances --instance-ids i-078b5f97b4a326395
aws ec2 wait instance-terminated --instance-ids i-078b5f97b4a326395
aws ec2 delete-security-group --group-id sg-de8e31a5
aws ec2 disassociate-route-table --association-id rtbassoc-3651874f
aws ec2 delete-route-table --route-table-id rtb-320ed554
aws ec2 detach-internet-gateway --internet-gateway-id igw-1e7d9479 --vpc-id vpc-517a5036
aws ec2 delete-internet-gateway --internet-gateway-id igw-1e7d9479
aws ec2 delete-subnet --subnet-id subnet-6e6b2d09
aws ec2 delete-vpc --vpc-id vpc-517a5036
echo If you want to delete the key-pair, please do it manually.
