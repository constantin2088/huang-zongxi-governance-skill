"""Report declared reviewer conflicts; undisclosed relationships remain unknown."""
def review(proposers,beneficiaries,reviewers):
 for group in (proposers,beneficiaries,reviewers):
  if not isinstance(group,list) or any(not isinstance(x,str) or not x.strip() for x in group):raise ValueError('lists of nonempty identifiers required')
  if len(set(group))!=len(group):raise ValueError('duplicate identifier')
 if not reviewers:raise ValueError('at least one reviewer required')
 interested=set(proposers)|set(beneficiaries)
 return {'declared_conflicts':sorted(set(reviewers)&interested),'no_declared_conflict':sorted(set(reviewers)-interested)}
