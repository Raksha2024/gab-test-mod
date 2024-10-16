output "cluster_id" {
  value = aws_eks_cluster.gab.id
}

output "node_group_id" {
  value = aws_eks_node_group.gab.id
}

output "vpc_id" {
  value = aws_vpc.gab_vpc.id
}

output "subnet_ids" {
  value = aws_subnet.gab_subnet[*].id
}