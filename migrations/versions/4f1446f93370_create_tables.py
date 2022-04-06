"""create tables

Revision ID: 4f1446f93370
Revises: 
Create Date: 2022-04-05 18:28:45.339497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f1446f93370'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    eisenhowers = op.create_table('eisenhowers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('importance', sa.Integer(), nullable=True),
    sa.Column('urgency', sa.Integer(), nullable=True),
    sa.Column('eisenhower_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['eisenhower_id'], ['eisenhowers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tasks_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    op.bulk_insert(
        eisenhowers,
        [
            {"type": "Do It First"},
            {"type": "Delegate It"},
            {"type": "Schedule It"},
            {"type": "Delete It"},
        ],
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks_categories')
    op.drop_table('tasks')
    op.drop_table('eisenhowers')
    op.drop_table('categories')
    # ### end Alembic commands ###